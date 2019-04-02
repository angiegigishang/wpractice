from mg_app_framework import app_start, set_store, set_config_func, set_init_task, TaskKey
from worksheet_manager.config import ConfigStore, MongodbConfig, RabbitMQConfig, IndexInit


async def config_process():
    pass


def main(debug_flag=True):
    set_store(ConfigStore())
    set_config_func(config_process)
    set_init_task([{TaskKey.mongodb: MongodbConfig()}, {TaskKey.rabbitmq_async: RabbitMQConfig()}, {TaskKey.init_func: IndexInit()}])
    app_start(debug_flag)
