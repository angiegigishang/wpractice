from worksheet_manager.utils.util import log_exception



bom_dict = {}
device_map = {}


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

        procedure_list = sorted(item['children'][0]['instance_list'], key=lambda x:x['name'])
        for procedure in procedure_list:

            per_procedure_info = {}
            per_procedure_info['name'] = procedure['children'][0]['instance_list'][0]['name']
            per_procedure_info['code'] = procedure['children'][0]['instance_list'][0]['code']

            m = procedure['children'][0]['instance_list'][0]['children']
            per_procedure_info['device'] = m[0]['instance_list']
            for i in per_procedure_info['device']:
                del i['children']
            # 去除原材料的配置
            # if len(m) == 1:
            #     per_procedure_info['material'] = []
            # else:
            #     per_procedure_info['material'] = m[1]['instance_list']
            #     for i in per_procedure_info['material']:
            #         del i['children']

            info['procedure'].append(per_procedure_info)

        bom_dict[code] = info
    # pprint(bom_dict)
    device_info()



worksheet_msg_handler = {'bom_zhuajuti': get_data}
worksheet_msg_keys = list(worksheet_msg_handler.keys())


def device_info():
    global device_map
    for product_code, product in bom_dict.items():
        for procedure in product['procedure']:
            for device in procedure['device']:
                device_map.update({device['code']: {'description': device['description'],
                                                    'name': device['name']}})
