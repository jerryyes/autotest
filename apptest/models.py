from django.db import models

# Create your models here.
class Appcase(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)# 关联产品ID
    appcasename = models.CharField('用例名称', max_length=200)      # 测试用例名称
    apptestresult = models.BooleanField('测试结果')      # 测试结果
    apptester = models.CharField('测试负责人', max_length=16)    # 执行人
    create_time = models.DateTimeField('创建时间', auto_now=True)   # 创建时间，自动获取当前时间

    class Meta:
        verbose_name = 'app 测试用例'
        verbose_name_plural = 'app 测试用例'

    def __str__(self):
        return self.appcasename


class Appcasestep(models.Model):
    Appcase = models.ForeignKey(Appcase,on_delete=models.CASCADE)  # 关联接口ID
    appteststep = models.CharField('测试步骤',max_length=200) # 测试步骤
    apptestobjname = models.CharField('测试对象名称描述',max_length=200) # 测试对象名称描述
    appfindmethod = models.CharField('定位方式', max_length=200)
    appevelement = models.CharField('控件元素', max_length=800)
    appoptmethod = models.CharField('操作方法', max_length=200)
    apptestdata = models.CharField('测试数据', max_length=200, null=True)  # 测试数据，临时增加字段时要设置可为空
    appassertdata = models.CharField('验证数据', max_length=200)    # 验证数据
    apptestresult = models.BooleanField('测试结果') # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)   # 创建时间，自动获取当前时间

    def __str__(self):
        return self.appteststep
