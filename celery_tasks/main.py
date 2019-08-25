from celery import Celery
import os


# 为celery使用django配置文件进行设置，注意main.py和settings.py的相对位置关系
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'autotest.settings'

# 创建celery对象,并起别名
celery_app = Celery('celery_tasks',include=['celery_tasks.apitest.tasks'])

#从配置文件加载配置
celery_app.config_from_object('celery_tasks.config')

#此时用定时任务来触发celery任务，因此不需要再注册celery任务
#celery_app.autodiscover_tasks(['celery_tasks.mail', 'celery_tasks.sms','celery_task.apitest'])
