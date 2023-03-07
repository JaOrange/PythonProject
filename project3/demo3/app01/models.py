from django.db import models

# Create your models here.


class Admin(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=64)
    password = models.CharField(verbose_name="密码", max_length=64)


class bjHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class shHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class tyHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class tjHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class xmHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class cqHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class sjzHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class hhhtHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class syHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class ccHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class hebHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class njHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class hzHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class hfHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class ncHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class jnHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class zzHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class whHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class csHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class gzHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class nnHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class hkHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class cdHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class gyHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class kmHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class xaHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class lzHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')

class wlmqHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class ycHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')


class szHouseInfo(models.Model):
    builder = models.CharField(max_length=256, verbose_name="开发商")
    houseType = models.CharField(max_length=64, verbose_name='户型')
    area = models.CharField(max_length=20, verbose_name='面积')
    direction = models.CharField(max_length=20, verbose_name='朝向')
    decoration = models.CharField(max_length=20, verbose_name='装修')
    floor = models.CharField(max_length=60, verbose_name='楼层')
    year = models.CharField(max_length=20, verbose_name='年份')
    structure = models.CharField(max_length=20, verbose_name='结构')
    total_price = models.CharField(max_length=20, verbose_name='售价(万元)')
    unit_price = models.CharField(max_length=20, verbose_name='单价(元/平方米)')