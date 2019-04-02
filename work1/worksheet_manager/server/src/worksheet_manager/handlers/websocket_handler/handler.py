import json
from collections import defaultdict

from mg_app_framework import WebsocketBasicHandler, get_logger

from worksheet_manager.utils.msg import bom_dict
from worksheet_manager.utils.util import get_date, get_worksheet_seq, get_time, get_worksheet_data, log_exception, \
    get_device_worksheet


class WorkSheetHandler(WebsocketBasicHandler):
    def open(self):
        print('websocket open')
        self.send_change()

    def on_message(self, message):
        try:
            message = json.loads(message)
            code = message.get("code")
            count = message.get("count")
            start_time = message.get("start_time")
            end_time = message.get("end_time")
            device_map = message.get("device")
            date = get_date()
            collection_worksheet = get_worksheet_seq()
            ret = collection_worksheet.find_one({'date': date})
            if ret is None:
                collection_worksheet.insert({'date': date, "worksheet_count": 0})
                worksheet_count = 1
            else:
                worksheet_count = ret['worksheet_count'] + 1
            worksheet_id = '%s%05d' % (date, worksheet_count)
            worksheet_dict = {
                'worksheet_id': worksheet_id,
                'code': code,
                'name': bom_dict[code]['name'],
                'num': count,
                'start_time': start_time,
                'end_time': end_time,
                'create_time': get_time(),
            }
            process_device_map = defaultdict(list)
            for process, device_list in device_map.items():
                for device in device_list:
                    process_device_map[device].append(process)
            for device_name, process_list in process_device_map.items():
                worksheet_dict.update({device_name: {'mark': '', 'procedure_list': process_list, 'data':{}}})
                for process in process_list:
                    worksheet_dict[device_name]['data'].update({process: []})
            collection_mark = get_worksheet_data()
            collection_mark.insert(worksheet_dict)
            collection_worksheet.update({'date': date}, {"$set": {"worksheet_count": worksheet_count}})
            del worksheet_dict['_id']
            get_logger().info('on_message {}'.format(worksheet_dict))
            worksheet_dict = json.dumps(worksheet_dict)
            self.write_message(worksheet_dict)
            self.send_change()
        except Exception as e:
            log_exception(e, '下发工单失败')
            self.write_message(None)

    def send_change(self):
        logger = get_logger()
        try:
            data_collection = get_worksheet_data()
            device_collection = get_device_worksheet()
            result = data_collection.find()
            ret_data = defaultdict(list)
            for item in result:
                for key, value in item.items():
                    if isinstance(value, dict):
                        if 'procedure_list' in list(value.keys()):
                            worksheet_id = item['worksheet_id']
                            one_worksheet = {'device_code': key, "worksheet_id": worksheet_id, "name": item['name'], "code": item['code'],
                                             "num": item['num'], "start_time": item["start_time"],
                                             "end_time": item["end_time"]}
                            ret = device_collection.find_one({'worksheet_id': worksheet_id})
                            if not ret:
                                state = 'complete'
                            else:
                                state = ret['state']
                            one_worksheet['state'] = state
                            one_worksheet['procedure'] = value['procedure_list']
                            ret_data[key].append(one_worksheet)
            logger.info("Get Worksheet data:{}".format(ret_data))
            ret_data = json.dumps(ret_data)
            self.write_message(ret_data)
        except Exception as e:
            log_exception(e, '获取工单信息失败')
            self.write_message('failed worksheet')

    def on_close(self):
        print('websocket on_close')
