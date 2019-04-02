from mg_app_framework import HttpBasicHandler, MesCode, TaskKey, get_handler
from tracebackapp.utils.msg import bom_dict, data_dict
from collections import defaultdict

"""
获取mongodb指定collection数据：
@collection str
@params {}
"""
def get_mongodb_data(collection, params):
    handler = get_handler(TaskKey.mongodb)
    data = handler.baoyiji[collection].find(params)
    result = []
    for row in data:
        del row["_id"]
        result.append(row)
    return result

def sum_worksheet_data(data):
    productList = data_dict['product']
    complete = defaultdict(int)
    for row in data:

        try:
            complete[row['code']] += row['num']
        except Exception as e:
            pass

        for p in productList:
            if row['code'] == p['code']:
                opFinish = defaultdict(int)
                deviceFinish = defaultdict(int)
                p['complete'] = complete[row['code']]
                for key, value in row.items():
                    if key.startswith('device_'):

                        for op in bom_dict[row['code']]['procedure']:
                            try:
                                opFinish[op['code']] = len(row[key]['data'][op['code']])
                            except Exception as e:
                                pass

                        for mark_list,mark_data in row[key]["data"].items():
                            try:
                                deviceFinish[key] += len(mark_data)
                            except Exception as e:
                                pass
                p['deviceFinish'] = deviceFinish
                p['opFinish'] = opFinish
    return productList
    


class ProductCompletionHandler(HttpBasicHandler):
    async def get_process(self, start_time, end_time):
        params = {
            'create_time': { "$gt": start_time },
            'create_time': { "$lt": end_time }
        }
        send_data = get_mongodb_data('worksheet_data', params)
        data = sum_worksheet_data(send_data)
        if data:
            self.send_response_data(MesCode.success, 
                                    data, 
                                    'success get data')
