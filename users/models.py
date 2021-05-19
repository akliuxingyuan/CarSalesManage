# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class Right(models.Model):
    authName = models.CharField(max_length=20, verbose_name="权限名称")
    authDesc = models.CharField(max_length=50, verbose_name="权限描述")

    class Meta:
        db_table = 'rights'
        verbose_name = '权限'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id) + ' ' + self.authName


class Role(models.Model):
    roleName = models.CharField(max_length=20, verbose_name="角色名称")
    roleDesc = models.CharField(max_length=50, verbose_name="角色描述")
    rights = models.ManyToManyField(Right)

    class Meta:
        db_table = 'roles'
        verbose_name = '用户角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.roleName


class User(AbstractUser):
    first_name = None
    last_name = None
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号")
    rid = models.ForeignKey(Role, on_delete=models.PROTECT, verbose_name="用户角色")

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
