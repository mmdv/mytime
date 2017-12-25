from django.db import models

# Create your models here.
class mytime(models.Model):
    name = models.IntegerField()#时间名称
    timeb = models.CharField(max_length=30)#开始时间
    timee = models.CharField(max_length=30)#结束时间
    order = models.IntegerField()#当天事件顺序

    def __str__(self):
        return '%s' % (self.name)