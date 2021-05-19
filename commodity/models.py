from django.db import models


# Create your models here.

class Category(models.Model):
    cat_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='分类ID')
    cat_name = models.CharField(max_length=20, verbose_name='分类名称')
    cat_pid = models.IntegerField(verbose_name='分类父ID')
    cat_level = models.IntegerField(verbose_name='分类层级')
    children = models.ManyToManyField('self', symmetrical=False, verbose_name='子分类集')

    class Meta:
        db_table = 'category'
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name


class Factory(models.Model):
    fid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='工厂ID')
    fname = models.CharField(max_length=20, verbose_name='工厂名称')
    faddress = models.CharField(max_length=20, verbose_name='工厂地址')

    class Meta:
        db_table = 'factory'
        verbose_name = '工厂'
        verbose_name_plural = verbose_name


class Car(models.Model):
    cid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='汽车ID')
    cname = models.CharField(max_length=20, verbose_name='商品名称')
    cbrand = models.CharField(max_length=20, verbose_name='汽车品牌')
    introduce = models.CharField(max_length=50, verbose_name='简介')
    pics = models.CharField(max_length=128, verbose_name='图片')
    cprice = models.FloatField(verbose_name='价格')
    fid = models.ForeignKey(Factory, on_delete=models.PROTECT, verbose_name='工厂ID')

    class Meta:
        db_table = 'car'
        verbose_name = '汽车'
        verbose_name_plural = verbose_name


class CustomerTrade(models.Model):
    ctid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='订单ID')
    ctprice = models.FloatField(verbose_name='成交价格')
    cprofit = models.FloatField(verbose_name='总利润')
    cid = models.ForeignKey(Car, on_delete=models.PROTECT, verbose_name='汽车ID')

    class Meta:
        db_table = 'customer_trade_data'
        verbose_name = '客户购买订单'
        verbose_name_plural = verbose_name


class FactoryTrade(models.Model):
    ftid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='订单ID')
    ftprice = models.FloatField(verbose_name='成交价格')
    fid = models.ForeignKey(Car, on_delete=models.PROTECT, verbose_name='厂商ID')

    class Meta:
        db_table = 'factory_trade_data'
        verbose_name = '工厂购入订单'
        verbose_name_plural = verbose_name
