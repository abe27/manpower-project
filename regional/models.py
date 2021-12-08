import uuid
from django.db import models

from employee.models import STATUS_CHOICES

# Create your models here.


class Province(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    code = models.CharField(
        max_length=255, unique=True, verbose_name=u'รหัส')
    province = models.CharField(
        max_length=255, unique=True, verbose_name=u'ชื่อ')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    latitude = models.DecimalField(null=True,
                                   decimal_places=18,
                                   max_digits=44, default=0, verbose_name=u'ละติจูด')
    longitude = models.DecimalField(null=True,
                                    decimal_places=18,
                                    max_digits=44, default=0, verbose_name=u'ลองจิจูด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลจังหวัด'
        db_table = "tbt_provinces"


class District(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    province_id = models.OneToOneField(
        Province, on_delete=models.CASCADE, verbose_name='จังหวัด')
    district = models.CharField(
        max_length=255, unique=True, verbose_name=u'ชื่อ')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    latitude = models.DecimalField(null=True,
                                   decimal_places=18,
                                   max_digits=44, default=0, verbose_name=u'ละติจูด')
    longitude = models.DecimalField(null=True,
                                    decimal_places=18,
                                    max_digits=44, default=0, verbose_name=u'ลองจิจูด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลอำเภอ'
        db_table = "tbt_districts"


class ZipCode(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    district_id = models.OneToOneField(
        District, on_delete=models.CASCADE, verbose_name='จังหวัด')
    zipcode = models.CharField(
        max_length=10, verbose_name=u'รหัสไปรษณีย์')
    tombon = models.CharField(
        max_length=255, verbose_name=u'ตำบล')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    latitude = models.DecimalField(null=True,
                                   decimal_places=18,
                                   max_digits=44, default=0, verbose_name=u'ละติจูด')
    longitude = models.DecimalField(null=True,
                                    decimal_places=18,
                                    max_digits=44, default=0, verbose_name=u'ลองจิจูด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลรหัสไปรษณีย์'
        db_table = "tbt_zipcodes"
