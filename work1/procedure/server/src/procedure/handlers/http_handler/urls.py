from procedure.handlers.http_handler.handler import *

url = [
    (r'/procedure/get_devices', GetDeviceHandler),  # 获取所有的设备，每个设备一个页面
    (r'/procedure/get_data', GetDataHandler),  # 获取主数据的相关东西
    (r'/procedure/get_my_worksheets/(?P<device_code>.*)', GetMyWorksheetHandler),  # 根据设备获取相应的工单

    (r'/procedure/start_worksheet', StartWorksheetHandler),  # 开始此设备的工单
    (r'/procedure/end_worksheet', EndWorksheetHandler),  # 终止此设备的工单

    (r'/procedure/record_mark_time', RecordMarkTimeHandler),  # 扫码记录

    # 获取工单和设备 页面的头部
    (r'/procedure/get_device_worksheet_info/(?P<device_code>.*)/(?P<worksheet_id>.*)', GetDeviceWorkSheetInfo),
    # 获取设备工单数据
    (r'/procedure/get_device_worksheet/(?P<device_code>.*)/(?P<worksheet_id>.*)', GetDeviceWorksheetHandler),
    # 获取这个工单 这个设备 这个工序的所有扫码数据
    (r'/procedure/get_history_data/(?P<device_code>.*)/(?P<worksheet_id>.*)/(?P<procedure_code>.*)', GetHistoryDataHandler),

    (r'/procedure/get_worksheet_data/(?P<worksheet_id>.*)', GetWorkSheetDataHandler)
]
