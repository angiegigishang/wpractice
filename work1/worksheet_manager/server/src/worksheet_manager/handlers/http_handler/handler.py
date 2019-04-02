import os
from collections import defaultdict

from mg_app_framework import HttpBasicHandler, MesCode, get_logger
from pymongo import UpdateOne

from worksheet_manager.utils.msg import bom_dict
from worksheet_manager.utils.util import get_worksheet_seq, log_exception, get_time, \
    get_worksheet_data, get_date, EXCEL_FILE_FOLDER, parse, get_inventory


class ProductHandler(HttpBasicHandler):
    async def get(self):
        ret_data = []
        for info in bom_dict.values():
            ret_data.append(info)
        self.send_response_data(MesCode.success, ret_data, 'success get data')


class PostWorkSheetHandler(HttpBasicHandler):
    async def post(self):
        try:
            code = self.data.get("code")
            count = self.data.get("count")
            start_time = self.data.get("start_time")
            end_time = self.data.get("end_time")
            device_map = self.data.get("device")
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
            get_logger().info(worksheet_dict)
            return self.send_response_data(MesCode.success, worksheet_dict, 'success worksheet')
        except Exception as e:
            log_exception(e, '下发工单失败')
            return self.send_response_data(MesCode.fail, None, 'failed worksheet')


class ExcelHandler(HttpBasicHandler):
    async def post(self):
        logger = get_logger()
        try:
            files = self.request.files
            file = files.get('file')[0]
            filename = file.get('filename')
            data = file.get('body')
            dir_path = filename
            with open(dir_path, 'wb') as f:
                f.write(data)
            ret = parse(dir_path)
            date = get_date()
            collection = get_inventory()
            collection.bulk_write([UpdateOne({'number': material_info['number']},
                                             {"$set": {"inventory": material_info["inventory"], "date": date}},
                                             upsert=True)
                                   for material_info in ret])
            logger.info('ExcelHandler input data:{}'.format(ret))
            return self.send_response_data(MesCode.success, ret, 'success input excel')
        except Exception as e:
            try:
                if os.path.exists(dir_path):
                    os.remove(dir_path)
            except NameError:
                pass
            log_exception(e, '导入excel失败')
            return self.send_response_data(MesCode.fail, None, 'failed input excel')
