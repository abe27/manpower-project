from ckeditor.fields import RichTextField
from django.db import models
import uuid

from master.models import STATUS_CHOICES, Department

# Create your models here.


class ActivitiesCategories(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=255, verbose_name=u'หัวข้อหมวดหมู่')
    descriptions = RichTextField(
        blank=True, null=True, verbose_name=u'รายละเอียด/ข้อมูลเพิ่มเติม')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลหมวดหมู่'
        db_table = "tbt_activitiescategories"


class ActivitiesChoise(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    category_id = models.OneToOneField(
        ActivitiesCategories, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=u'หมวดหมู่')
    title = models.CharField(max_length=255, verbose_name=u'หัวข้อ/เรื่อง')
    descriptions = RichTextField(
        blank=True, null=True, verbose_name=u'รายละเอียด/ข้อมูลเพิ่มเติม')
    full_score = models.DecimalField(decimal_places=18, max_digits=44,
                                     blank=True, null=True, default=0, verbose_name='คะแนนเต็ม')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลหัวข้อ/เรื่อง'
        db_table = "tbt_activitieschoies"


class ActivitiesForOrganization(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    activities_id = models.OneToOneField(
        ActivitiesChoise, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=u'หัวข้อ/เรื่อง')
    department_id = models.ForeignKey(
        Department, on_delete=models.CASCADE, verbose_name=u'หัวข้อ/แผนก')
    descriptions = RichTextField(
        blank=True, null=True, verbose_name=u'รายละเอียด/ข้อมูลเพิ่มเติม')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลหัวข้อ/เรื่อง สำหรับแผนก'
        db_table = "tbt_activitiesorgans"


class ActivitiesCleanup(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    activities_date = models.DateField(verbose_name='วันที่ทำกิจกรรม')
    activities_id = models.OneToOneField(
        ActivitiesForOrganization, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=u'หัวข้อ/เรื่อง')
    descriptions = RichTextField(
        blank=True, null=True, verbose_name=u'รายละเอียด/ข้อมูลเพิ่มเติม')
    score = models.DecimalField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')], decimal_places=18, max_digits=44,
                                blank=True, null=True, default=0, verbose_name='คะแนนที่ได้')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลการทำกิจกรรม 5 ส'
        db_table = "tbt_activitiescleanups"


class ImagesActivites(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    squize_id = models.ForeignKey(
        ActivitiesCleanup, on_delete=models.CASCADE, verbose_name=u'หัวข้อ')
    image = models.FileField(verbose_name=u'รูปประกอบ')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลเอกสารประกอบการทำกิจกรรม 5 ส'
        db_table = "tbt_imagesactivities"
