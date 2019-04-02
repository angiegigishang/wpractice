import os
import traceback
import datetime
from enum import unique, Enum

import xlrd
from mg_app_framework import TaskKey, get_handler, get_logger


EXCEL_FILE_FOLDER = '/root/workspace/excel_file_folder/'


def log_exception(e, err_info):
    traceback_str = ''.join(traceback.format_tb(e.__traceback__))
    err_msg = '程序错误信息: {}, 异常信息: {}\n'.format(err_info, str(e))
    get_logger().error(err_msg)
    get_logger().error('traceback信息: {}'.format(traceback_str))


def get_worksheet_seq():
    handler = get_handler(TaskKey.mongodb)
    return handler.baoyiji.worksheet_seq


def get_worksheet_data():
    handler = get_handler(TaskKey.mongodb)
    return handler.baoyiji.worksheet_data


def get_device_worksheet():
    handler = get_handler(TaskKey.mongodb)
    return handler.baoyiji.device_worksheet


def get_mark_worksheet():
    handler = get_handler(TaskKey.mongodb)
    return handler.baoyiji.mark_worksheet


def get_inventory():
    handler = get_handler(TaskKey.mongodb)
    return handler.baoyiji.inventory


class Tables(object):
    # 工单今日计数
    worksheet_seq = 'worksheet_seq'
    # 工单数据
    worksheet_data = 'worksheet_data'

    # 设备绑定工单： 设备，工单，绑定时间，取消绑定时间，操作人工号，操作人名称，状态（running complete）
    device_worksheet = 'device_worksheet'

    # 刻码和工单映射关系
    mark_worksheet = 'mark_worksheet'

    # 材料库存表
    inventory = 'inventory'


def get_date():
    return datetime.datetime.now().strftime('%Y%m%d')


def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def parse(file_name):
    wb = xlrd.open_workbook(file_name)
    ws = wb.sheet_by_index(0)
    rows = ws.nrows
    ret_data = []
    for row in range(1, rows):
        ret_data.append({'warehouse': str(ws.row_values(row)[0]),
                         'number': str(ws.row_values(row)[1]),
                         'material': str(ws.row_values(row)[2]),
                         'inventory': int(ws.row_values(row)[6])})
    os.remove(file_name)
    return ret_data
