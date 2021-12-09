from ckeditor.fields import RichTextField
from django.db import models
import uuid
from employee.models import Profile

from master.models import STATUS_CHOICES, LeaveType

APPROVE_CHOICES = [
    (0, '-'), (1, 'Reject'), (2, 'Approved')
]

STATUS_SENDMAIL_CHOICES = [
    (False, 'ยังไม่ส่ง'),
    (True, 'ส่งแล้ว')
]

# Create your models here.


class Leave(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    user_id = models.OneToOneField(
        Profile, on_delete=models.CASCADE, verbose_name=u'ชื่อพนักงาน')
    leave_type_id = models.OneToOneField(
        LeaveType, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=u'ประเภทที่ลา')
    leave_on = models.DateField(verbose_name=u'วันที่ลา')
    from_time = models.TimeField(verbose_name=u'เริ่มจากเวลา')
    to_time = models.TimeField(verbose_name=u'ถึงเวลา')
    reason = models.TextField(verbose_name=u'สาเหตุที่ลา/เหตุผล')
    descriptions = RichTextField(
        blank=True, null=True, default='-', verbose_name=u'ข้อมูลเพิ่มเติม')
    total_leave = models.DecimalField(
        null=True, decimal_places=18, max_digits=44, default=0, verbose_name=u'ผลรวม')
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

    class Meta:
        # abstract = True
        verbose_name_plural = u'บันทึกข้อมูลการลา'
        db_table = "tbt_leaves"


class AttachmentLeave(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    leave_id = models.ForeignKey(
        Leave, on_delete=models.CASCADE, verbose_name=u'หัวข้อการลา')
    attachment = models.FileField(verbose_name=u'เอกสารประกอบการลา')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'บันทึกข้อมูลเอกสารประกอบการลา'
        db_table = "tbt_attachmentleaves"
