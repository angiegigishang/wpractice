from os.path import dirname, realpath, basename, join
from mg_app_framework import AppConfigBasic, AppType, MongodbConfigBasic, RabbitMQConfigBasic
from procedure.utils.msg import worksheet_msg_keys, worksheet_msg_processor

class ConfigStore(AppConfigBasic):
    # ==================== DON'T MODIFY THE CODE BETWEEN COMMENT LINE ====================

    work_dir = dirname(dirname(dirname(realpath(__file__))))
    app = basename(dirname(realpath(__file__)))
    log_path = join(work_dir, 'log', app + '.log')
    uuid_path = join(work_dir, '.appid')

    def get_module_dir(self):
        return dirname(realpath(__file__))

    def get_log_path(self):
        return self.log_path

    def get_uuid_path(self):
        return self.uuid_path

    def get_data(self):
        return self.data

    # ==================== DON'T MODIFY THE CODE BETWEEN COMMENT LINE ====================

    data = {
        'app_group': '包头一机厂app',
        'app_name': '工序',
        'app_type': AppType.user,
        'config_create': True,
        'data': {}
    }

    def get_admin_host(self):
        return '192.168.250.247'

    def get_app_port(self):
        return 9000

    def connect_admin(self):
        return True

    def cross_domain(self):
        return False


class MongodbConfig(MongodbConfigBasic):
    def get_mongodb_host(self):
        return '192.168.250.247'

    def get_mongodb_port(self):
        return '27017'


class RabbitMQConfig(RabbitMQConfigBasic):
    # 配置ip
    def get_rabbitmq_host(self):
        return '192.168.250.247'

    # 配置port
    def get_rabbitmq_port(self):
        return '5672'

    # 配置用户名
    def get_rabbitmq_username(self):
        return 'rabbitmq'

    # 配置密码
    def get_rabbitmq_password(self):
        return 'rabbitmq'

    # 打开发布配置数据开关
    def publish_config_data(self):
        return False

    def get_rabbitmq_subscribe_list(self):
        return worksheet_msg_keys

    # 注册消息分发与处理入口函数
    def messsge_process_func(self):
        return worksheet_msg_processor