from mg_app_framework import get_logger
from tracebackapp.utils.util import log_exception
import collections
from pprint import pprint

data_dict = {}
bom_dict = {}


async def worksheet_msg_processor(data):
    try:
        msg_key = data['key']
        msg_data = data['data']
        if msg_key in worksheet_msg_handler:
            worksheet_msg_handler[msg_key](msg_data)
    except Exception as e:
        log_exception(e, '处理rabbitmq消息异常')


def get_data(msg):
    for item in msg['children'][0]['instance_list']:
        name = item['name']
        code = item['code']
        info = {}
        info['name'] = name
        info['code'] = code
        info['procedure'] = []

        procedure_list = sorted(item['children'][0]['instance_list'], key=lambda x: x['name'])
        for procedure in procedure_list:

            per_procedure_info = {}
            per_procedure_info['name'] = procedure['children'][0]['instance_list'][0]['name']
            per_procedure_info['code'] = procedure['children'][0]['instance_list'][0]['code']

            m = procedure['children'][0]['instance_list'][0]['children']
            per_procedure_info['device'] = m[0]['instance_list']
            for i in per_procedure_info['device']:
                del i['children']
            # if len(m) == 1:
            #     per_procedure_info['material'] = []
            # else:
            #     per_procedure_info['material'] = m[1]['instance_list']
            #     for i in per_procedure_info['material']:
            #         del i['children']

            info['procedure'].append(per_procedure_info)

        bom_dict[code] = info


def get_product(msg):
    # 根据产品实体获取所有产品
    data_dict['product'] = msg['instance_list']


def get_device(msg):
    # 获取所有设备详情
    data_dict['device'] = msg['instance_list']


def get_procedure(msg):
    data_dict['procedure'] = msg['instance_list']


worksheet_msg_handler = {'bom_zhuajuti': get_data, 'product': get_product, 'device': get_device,
                         'procedure': get_procedure}
worksheet_msg_keys = list(worksheet_msg_handler.keys())
