a = {'code': 'product_bisuoxiaoti',
     'create_time': '2019-03-22 18:05:42',
     'device_31301010161': {
         'mark': '',
         'procedure_list': ['procedure_y_30'],
         'data': {
             'procedure_y_30': [],
         }},
     'device_3270101047': {
         'mark': '',
         'procedure_list': ['procedure_y_35'],
         'data': {
             'procedure_y_35': []
         }},
     'device_3270101161': {
         'mark': '',  # 正在做哪个刻码
         'procedure_list': ['procedure_y_40', 'procedure_y_45'],
         'data': {
             'procedure_y_40': [],
             'procedure_y_45': []
         }
     },

     'end_time': '2019-03-23',
     'name': '闭锁销体',
     'num': 10,
     'start_time': '2019-03-21',
     'worksheet_id': '2019032600001'}

import pymongo
client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client.test.test
from datetime import datetime

print(db.update({'abc': datetime.now()}, {'$set':{'a':'mmm'}}))


# db = client.baoyiji.worksheet_data_test
#
# db.insert(a)