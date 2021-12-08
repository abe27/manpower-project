import uuid
from django.db import models
from employee.models import Profile

from master.models import STATUS_APPROVE_CHOICES, STATUS_CHOICES

# Create your models here.


class TimeAttendModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    user_id = models.OneToOneField(
        Profile, on_delete=models.CASCADE, verbose_name=u'พนักงาน')
    record_in = models.DateTimeField(
        blank=True, verbose_name=u'เข้าที่ทำงานเมื่อ')
    record_out = models.DateTimeField(
        blank=True, verbose_name=u'ออกจากที่ทำงานเมื่อ')
    is_change_shift = models.BooleanField(
        choices=STATUS_APPROVE_CHOICES, default=False, blank=True, verbose_name=u'เปลี่ยนกะ')
    descriptions = models.TextField(
        blank=True, verbose_name=u'ข้อมูลเพิ่มเติม')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลบันทึกเวลาเข้าทำงาน'
        db_table = "tbt_timeattendances"


class ImageTimeAttendance(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    training_id = models.ForeignKey(
        TimeAttendModel, on_delete=models.CASCADE, verbose_name=u'หัวข้อ')
    image = models.ImageField(null=True, blank=True)
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลรูปภาพประกอบบันทึกเวลาเข้าทำงาน'
        db_table = "tbt_illustrationtimeattendances"
