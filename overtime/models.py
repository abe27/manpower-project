from ckeditor.fields import RichTextField
from django.db import models
import uuid
from employee.models import Profile
from leave.models import APPROVE_CHOICES, STATUS_SENDMAIL_CHOICES
from master.models import STATUS_APPROVE_CHOICES, STATUS_CHOICES

# Create your models here.


class OverTime(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, verbose_name=u'ชื่อพนักงาน')
    subject = models.CharField(
        max_length=255, verbose_name=u'หัวข้อ')
    from_datetime = models.DateTimeField(verbose_name=u'วันที่เริ่ม')
    to_datetime = models.DateTimeField(verbose_name=u'สิ้นสุดที่')
    descriptions = RichTextField(blank=True, verbose_name=u'รายละเอียด')
    is_holiday = models.BooleanField(choices=STATUS_APPROVE_CHOICES,
                                     blank=True, default=False, verbose_name=u'วันหยุดตามปฎิทินของบริษัท', editable=False)
    # ///ตรวจสอบจากข้อมูล calendar ของบริษัท
    leader_approve = models.IntegerField(
        null=True, blank=True, choices=APPROVE_CHOICES, verbose_name=u'หัวหน้างาน/สถานะ')
    leader_approve_at = models.DateField(
        blank=True, null=True, verbose_name=u'หัวหน้า/อัพเดทข้อมูลเมื่อ')
    leader_comment = models.TextField(
        blank=True, null=True, verbose_name=u'หัวหน้า/ข้อมูลเพิ่มเติม')
    mgr_approve = models.IntegerField(
        null=True, blank=True, choices=APPROVE_CHOICES, verbose_name=u' ผู้จัดการ/สถานะ')
    mgr_approve_at = models.DateField(
        blank=True, null=True, verbose_name=u'ผู้จัดการ/อัพเดทข้อมูลเมื่อ')
    mgr_comment = models.TextField(
        blank=True, null=True, verbose_name=u'ผู้จัดการ/ข้อมูลเพิ่มเติม')
    hr_approve = models.IntegerField(
        null=True, blank=True, choices=APPROVE_CHOICES, verbose_name=u'พนักงานทัพยากรบุคคล/สถานะ')
    hr_approve_at = models.DateField(
        blank=True, null=True, verbose_name=u'พนักงานทัพยากรบุคคล/อัพเดทข้อมูลเมื่อ')
    hr_comment = models.TextField(
        blank=True, null=True, verbose_name=u'พนักงานทัพยากรบุคคล/ข้อมูลเพิ่มเติม')
    sendmail = models.BooleanField(
        choices=STATUS_SENDMAIL_CHOICES, default=False, verbose_name=u'สถานะการส่งเมล์')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'บันทึกข้อมูลทำงานล่วงเวลา'
        db_table = "tbt_overtimes"
