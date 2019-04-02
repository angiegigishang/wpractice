from worksheet_manager.handlers.http_handler.handler import *

url = [
    (r'/worksheet_manage/get_product', ProductHandler),  # 获取产品
    (r'/worksheet_manage/post_worksheet', PostWorkSheetHandler),  # 下工单
    (r'/worksheet_manage/excel', ExcelHandler)
]


