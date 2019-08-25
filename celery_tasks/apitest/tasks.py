from celery_tasks.main import celery_app
from celery.utils.log import get_task_logger

logger = get_task_logger('getSum')

# 此定时任务是定时对 1-n 的数列求和
@celery_app.task(name='celery_tasks.apitest.tasks.getSum')
def getSum(n):
    rangelist = []
    sum = 0
    for i in range(1, n):
        sum += i
        rangelist.append(str(i))
    SumExp = '+'.join(rangelist)
    print("%s = %s" % (SumExp, sum))
    logger.info("GETSUM task run success. The result is : %s = %s" % (SumExp, sum))
    return SumExp, sum
