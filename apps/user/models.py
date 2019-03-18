from django.db import models


class User(models.Model):
    """
    用戶信息
    """
    name = models.CharField(max_length=30, verbose_name='用戶名')
    email = models.EmailField(max_length=30, verbose_name='邮箱')
    number = models.CharField(max_length=30, verbose_name='工号', unique=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
