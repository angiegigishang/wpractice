from mg_app_framework import HttpBasicHandler, MesCode, get_logger
from procedure.utils.util import log_exception, get_time, mark_parse, get_device_worksheet, get_worksheet_data, \
    get_worksheet_seq, get_mark_worksheet
from procedure.utils.msg import bom_dict, data_dict
from pymongo import ReturnDocument


class BaoyijiHandler(HttpBasicHandler):
    def get_device_info(self, device_code):
        return [x for x in data_dict['device'] if x['code'] == device_code][0]

    def get_procedure_info(self, procedure_code):
        return [x for x in data_dict['procedure'] if x['code'] == procedure_code][0]

    def get_product_info(self, product_code):
        return [x for x in data_dict['product'] if x['code'] == product_code][0]


class GetDeviceHandler(HttpBasicHandler):
    async def get(self):
        self.send_response_data(MesCode.success, data_dict['device'], 'success worksheet')


class GetDataHandler(HttpBasicHandler):
    async def get(self):
        self.send_response_data(MesCode.success, data_dict, 'success worksheet')


class GetMyWorksheetHandler(BaoyijiHandler):
    async def get(self, device_code):
        logger = get_logger()
        try:
            data_collection = get_worksheet_data()
            device_collection = get_device_worksheet()
            result = data_collection.find({device_code: {'$exists': 'true'}})
            ret_data = []
            for item in result:
                worksheet_id = item['worksheet_id']
                one_worksheet = {"worksheet_id": worksheet_id, "name": item['name'], "code": item['code'],
                                 "num": item['num'], "start_time": item["start_time"],
                                 "end_time": item["end_time"]}
                ret = device_collection.find_one({'worksheet_id': worksheet_id, 'device_code': device_code})
                person_name = ''
                person_id = ''
                if not ret:
                    state = 'complete'
                else:
                    state = ret['state']
                    person_name = ret['person_name']
                    person_id = ret['person_id']
                one_worksheet['procedure'] = [self.get_procedure_info(x) for x in item[device_code]['procedure_list']]
                one_worksheet['state'] = state
                one_worksheet['person_name'] = person_name
                one_worksheet['person_id'] = person_id
                ret_data.append(one_worksheet)
            logger.info("GetMyWorksheetHandler get data:{}".format(ret_data))
            self.send_response_data(MesCode.success, ret_data, 'success worksheet')
        except Exception as e:
            log_exception(e, '获取工单信息失败')
            return self.send_response_data(MesCode.fail, None, 'failed worksheet')


class StartWorksheetHandler(HttpBasicHandler):
    async def post(self):
        # 根据工单、设备开始。 一个设备在同一时刻只能run一个工单
        #  把设备 和工单的关系 人员信息保存在一个表里面 device_worksheet
        worksheet_id = self.data['worksheet_id']
        device_code = self.data['device_code']
        person_id = self.data['person_id']
        person_name = self.data['person_name']

        db = get_device_worksheet()

        result = db.find_one({'device_code': device_code, 'state': 'running'})
        if result:
            #  该设备已经绑定了工单
            del result['_id']
            return self.send_response_data(MesCode.fail, result, 'has bind other worksheet')
        else:
            # 同一个设备 同一个工单 在device_worksheet 表中只能有一条记录
            result = db.find_one_and_update({'worksheet_id': worksheet_id, 'device_code': device_code},
                                            {'$set': {'bind_time': get_time(), 'state': 'running',
                                                      'person_id': person_id, 'person_name': person_name
                                                      }}, upsert=True, return_document=ReturnDocument.AFTER)
            del result['_id']
        self.send_response_data(MesCode.success, result, 'success')


class EndWorksheetHandler(HttpBasicHandler):
    async def post(self):
        worksheet_id = self.data['worksheet_id']
        device_code = self.data['device_code']

        db = get_device_worksheet()

        result = db.find_one_and_update({'worksheet_id': worksheet_id, 'device_code': device_code, 'state': 'running'},
                                        {'$set': {'state': 'complete', 'unbind_time': get_time()}},
                                        return_document=ReturnDocument.AFTER)
        if not result:
            # 没有匹配上返回None
            return self.send_response_data(MesCode.fail, {}, 'not match ')
        del result['_id']
        self.send_response_data(MesCode.success, result, 'success')


class RecordMarkTimeHandler(BaoyijiHandler):
    async def post(self):
        # 1 前端传过来的device_code worksheet_id 去device_worksheet 查，是否是绑定关系。
        # 2 上料和下料的mark要一致。
        # 3 mark 和 worksheet 对应关系要写在mark_worksheet 表中。

        worksheet_id = self.data['worksheet_id']
        device_code = self.data['device_code']
        procedure_code = self.data['procedure_code']
        mark = self.data['mark']
        mark_time = self.data['mark_time']
        state = self.data['state']  # state: start, end

        # 扫码枪扫出来后8位是零件号， 与主数据匹配 找到相应的产品
        mark_info = mark_parse(mark)
        product_info = {}
        for p in data_dict['product']:
            if p['component_num'] == mark_info['component_num']:
                product_info = p
        if not product_info:
            return self.send_response_data(MesCode.fail, {}, 'wrong mark')

        # 判定绑定状态，获取人员信息
        active_info = get_device_worksheet().find_one({'device_code': device_code, 'worksheet_id': worksheet_id,
                                                       'state': 'running'})
        if not active_info:
            # 设备 和 工单 不是绑定状态
            return self.send_response_data(MesCode.fail, {}, 'not running')
        person_id = active_info['person_id']
        person_name = active_info['person_name']

        worksheet_data = get_worksheet_data().find_one({'worksheet_id': worksheet_id})
        if not worksheet_data:
            return self.send_response_data(MesCode.fail, {}, 'success worksheet')

        if state == 'start':
            # 上料
            insert_dict = {'mark': mark, 'start': mark_time, 'person_name': person_name, 'person_id': person_id,
                           'product_info': product_info, 'end': '',
                           'procedure_name': self.get_procedure_info(procedure_code)['name']}

            v = device_code + '.' + 'data' + '.' + procedure_code
            v1 = device_code + '.' + 'mark'
            get_worksheet_data().update({'worksheet_id': worksheet_id}, {'$push': {v: insert_dict},
                                                                         '$set': {v1: mark,
                                                                                  'last_active_time': mark_time}})

            # 保存mark 和工单的映射关系
            if not get_mark_worksheet().find_one({'mark': mark}):
                get_mark_worksheet().insert({'mark': mark, 'worksheet_id': worksheet_id})

        elif state == 'end':
            # 下料
            mark_list = worksheet_data[device_code]['data'][procedure_code]
            count = len(mark_list)
            if mark_list[-1]['mark'] != mark:
                return self.send_response_data(MesCode.fail, {}, 'start end mark not match')

            v = device_code + '.' + 'data' + '.' + procedure_code + '.' + str(count - 1) + '.' + 'end'
            get_worksheet_data().update({'worksheet_id': worksheet_id}, {'$set': {v: mark_time,
                                                                                  'last_active_time': mark_time}})

        product_info['person_name'] = person_name
        product_info['person_id'] = person_id
        return self.send_response_data(MesCode.success, product_info, 'success worksheet')


class GetHistoryDataHandler(HttpBasicHandler):
    async def get(self, device_code, worksheet_id, procedure_code):
        db = get_worksheet_data()
        history_data = db.find_one({'worksheet_id': worksheet_id})
        if not history_data:
            return self.send_response_data(MesCode.success, [], 'empty')

        self.send_response_data(MesCode.success, history_data[device_code]['data'][procedure_code], 'success')


class GetDeviceWorksheetHandler(BaoyijiHandler):
    async def get(self, device_code, worksheet_id):
        # 1 获取设备、工单的工序列表   2 可能存在的一个刻码（未完全走完这个设备）的数据
        db = get_worksheet_data()
        history_data = db.find_one({'worksheet_id': worksheet_id})
        if not history_data:
            return self.send_response_data(MesCode.success, {}, 'empty')

        device_data = history_data[device_code]
        result = {'procedure_info': [],
                  'data': []}
        mark = device_data['mark']
        if not mark:
            # 还没开始
            for procedure_code in device_data['procedure_list']:
                result['procedure_info'].append(self.get_procedure_info(procedure_code))
            return self.send_response_data(MesCode.success, result, 'success')

        for procedure_code in device_data['procedure_list']:
            result['procedure_info'].append(self.get_procedure_info(procedure_code))

            if len(device_data['data'][procedure_code]) > 0:
                # 把这个设备最后一个刻码的数据拿出来
                this_last_mark_info = device_data['data'][procedure_code][-1]
                if this_last_mark_info['mark'] == mark:
                    result['data'].append(this_last_mark_info)

        # 校验设备最后一个刻码的数据是否已经是结束的
        is_end = False
        if len(result['data']) == len(result['procedure_info']):
            for item in result['procedure_info']:
                if not item.get('end'):
                    # 有一个不存在就跳出循环
                    break
            else:
                # 所有的工序都有end时间，完成了
                is_end = True
        if is_end:
            result['data'] = []

        self.send_response_data(MesCode.success, result, 'success')


class GetDeviceWorkSheetInfo(BaoyijiHandler):
    async def get(self, device_code, worksheet_id):
        db = get_worksheet_data()
        history_data = db.find_one({'worksheet_id': worksheet_id})
        if not history_data:
            return self.send_response_data(MesCode.success, {}, 'empty')

        result = dict()
        result['device_info'] = self.get_device_info(device_code)

        result['worksheet_info'] = {'worksheet_id': worksheet_id,
                                    'start_time': history_data['start_time'],
                                    'end_time': history_data['end_time'],
                                    'num': str(history_data['num']),
                                    'product': history_data['name']}

        if get_device_worksheet().find_one(
                {'device_code': device_code, 'worksheet_id': worksheet_id, 'state': 'running'}):
            result['state'] = 'running'
        else:
            result['state'] = 'complete'

        self.send_response_data(MesCode.success, result, 'success')


class GetWorkSheetDataHandler(BaoyijiHandler):
    async def get(self, worksheet_id):
        # 获取到这个工单的数据。
        pass
