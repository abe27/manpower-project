from ckeditor.fields import RichTextField
from django.db import models
import uuid

from master.models import STATUS_CHOICES
from employee import models as emp

# Create your models here.
CHOICES_ACCEPT = [('-', '-'), ('N', 'ไม่ยอรับ'), ('A', 'ยอมรับ')]
CHOICES_PASS_OR_NOT = [('-', '-'), ('N', 'ไม่ผ่าน'), ('P', 'ผ่าน')]


class EvaluationGroup(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = RichTextField(blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลประเภทการประเมิน'
        db_table = "tbt_evaluationgroups"


class EvaluationLength(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    evaluate_group = models.OneToOneField(
        EvaluationGroup, on_delete=models.CASCADE, verbose_name=u'ประเภทการการประเมิน')
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = RichTextField(blank=True, verbose_name=u'รายละเอียด')
    score = models.DecimalField(
        blank=True, decimal_places=18, max_digits=44, default=0.0, verbose_name=u'ช่วงคะแนน')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลช่องคะแนนการประเมิน'
        db_table = "tbt_evaluationlengths"


class Evaluation(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    evaluate_group = models.OneToOneField(
        EvaluationGroup, on_delete=models.CASCADE, verbose_name=u'ประเภทการการประเมิน')
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = RichTextField(blank=True, verbose_name=u'รายละเอียด')
    score = models.DecimalField(
        blank=True, decimal_places=18, max_digits=44, default=0.0, verbose_name=u'คะแนนเต็ม')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลการประเมิน'
        db_table = "tbt_evaluations"


class EvaluationDetail(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    evaluate_id = models.OneToOneField(
        Evaluation, on_delete=models.CASCADE, verbose_name=u'หัวข้อการประเมิน')
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = RichTextField(blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลการประเมินเพิ่มเติม'
        db_table = "tbt_evaluationdetails"


class Evaluated(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    evaluate_id = models.OneToOneField(
        Evaluation, on_delete=models.CASCADE, verbose_name=u'หัวข้อการประเมิน')
    profile_id = models.OneToOneField(
        emp.Profile, on_delete=models.CASCADE, verbose_name=u'ผู้ถูกประเมิน')
    evaluate_date = models.DateTimeField(
        blank=True, null=True, verbose_name=u'วันที่ประเมิน')
    evaluate_score = models.DecimalField(
        blank=True, null=True, decimal_places=18, max_digits=44, default=0, verbose_name=u'คะแนนที่ได้')
    evaluate_status = models.CharField(
        max_length=1, choices=CHOICES_PASS_OR_NOT, blank=True, null=True, verbose_name=u'สถานะ')
    evaluate_comment = models.TextField(
        blank=True, null=True, verbose_name=u'ข้อเสนอแนะ')
    is_accept = models.CharField(
        blank=True, null=True, max_length=1, choices=CHOICES_ACCEPT, verbose_name=u'การยอมรับ')
    is_not_accept = models.TextField(
        blank=True, null=True, verbose_name=u'ข้อเสนอแนะ/กรณีไม่ยอมรับ/เหตุผลอื่นๆ')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลพนักงานที่ทำการประเมินเสร็จแล้ว'
        db_table = "tbt_evaluateds"


class EvaluatedDetail(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    profile_id = models.OneToOneField(
        Evaluated, on_delete=models.CASCADE, verbose_name=u'พนักงานที่ถูกประเมิน')
    evaluate_id = models.OneToOneField(
        EvaluationDetail, on_delete=models.CASCADE, verbose_name=u'หัวข้อการประเมิน')
    score_length = models.OneToOneField(
        EvaluationLength, on_delete=models.CASCADE, verbose_name=u'คะแนนที่ได้')
    remark = models.TextField(
        blank=True, null=True, verbose_name=u'ข้อเสนอแนะ')
    is_accept = models.CharField(
        choices=CHOICES_ACCEPT, max_length=1, blank=True, null=True, verbose_name=u'ยอมรับ')
    is_not_accept_remark = models.TextField(
        blank=True, null=True, verbose_name=u'ข้อเสนอแนะ/กรณีไม่ยอมรับ/เหตุผลอื่นๆ')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลพนักงานที่ทำการประเมินเพิ่มเติม'
        db_table = "tbt_evaluateddetails"
