from ckeditor.fields import RichTextField
from django.db import models
import uuid
from employee.models import Profile

from master.models import STATUS_CHOICES, Whs

# Create your models here.


class AccidentGroup(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    accident_type = models.CharField(max_length=1, choices=[(
        'C', 'Corrective'), ('D', 'Defective')], verbose_name=u'ประภท')
    title = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name=u'หัวข้อ')
    descriptions = RichTextField(blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลประเภทอุบัติเหตุ'
        db_table = "tbt_accidentgroups"


class Accident(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    whs_id = models.OneToOneField(
        Whs, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=u'พื้นที่เกิดอุบัติเหตุ')
    profile_id = models.OneToOneField(
        Profile, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=u'ผู้ที่ทำให้เกิอุบัติเหตุ')
    accident_group_id = models.ForeignKey(
        AccidentGroup, on_delete=models.CASCADE, verbose_name="ประเภทของอุบัติเหติ")
    title = models.CharField(max_length=255, blank=True,
                             null=True, verbose_name=u'หัวข้อ')
    on_date = models.DateField(verbose_name=u'วันที่')
    on_time = models.TimeField(verbose_name=u'เวลา')
    descriptions = RichTextField(
        blank=True, verbose_name=u'รายละเอียด/ข้อมูลเพิ่มเติม')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลการเกิดอุบัติเหตุ'
        db_table = "tbt_accidents"


class ImagesAccident(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    training_id = models.ForeignKey(
        Accident, on_delete=models.CASCADE, verbose_name=u'หัวข้อ')
    image = models.FileField(verbose_name=u'รูป/เอกสารประกอบ')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลรูปภาพประกอบการเกิดอุบัติเหตุ'
        db_table = "tbt_imageaccidents"


class ApproveAccident(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    profile_id = models.OneToOneField(
        Profile, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=u'ผู้รับเรื่อง')
    accident_id = models.ForeignKey(
        Accident, on_delete=models.CASCADE, verbose_name="หัวข้ออุบัติเหติ")
    descriptions = RichTextField(
        blank=True, null=True, verbose_name=u'แนวทางแก้/ข้อเสนอแนะ')
    is_approve = models.BooleanField(choices=[(
        False, '-'), (True, 'รับทราบ')], blank=True, null=True, default=False, verbose_name=u'รับทราบ')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลรับทราบเรื่องอุบัติเหตุ'
        db_table = "tbt_approveaccidents"
