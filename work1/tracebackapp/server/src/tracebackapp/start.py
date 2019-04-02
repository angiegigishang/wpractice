from mg_app_framework import app_start, set_store, set_config_func, set_init_task, TaskKey
from tracebackapp.config import ConfigStore, MongodbConfig, RabbitMQConfig


async def config_process():
    pass


def main(debug_flag=True):
    set_store(ConfigStore())
    set_config_func(config_process)
    set_init_task([
        {TaskKey.mongodb: MongodbConfig()},
        {TaskKey.rabbitmq_async: RabbitMQConfig()}
    ])

    app_start(debug_flag)
