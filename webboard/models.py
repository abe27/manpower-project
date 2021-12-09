import uuid
from django.db import models
from employee.models import Profile
from ckeditor.fields import RichTextField

from master.models import STATUS_CHOICES, Categories

# Create your models here.


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    category_id = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=u'หมวดหมู่')
    created_by = models.OneToOneField(
        Profile, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=u'สร้างโดย', editable=False)
    title = models.CharField(max_length=255, verbose_name=u'หัวข้อ/เรื่อง')
    descriptions = RichTextField(verbose_name=u'รายละเอียด/ข้อมูลเพิ่มเติม')
    total_views = models.IntegerField(
        blank=True, null=True, default=0, verbose_name='จำนวนผู้อ่าน')
    total_like = models.IntegerField(
        blank=True, null=True, default=0, verbose_name='จำนวนที่ชอบ')
    total_dislike = models.IntegerField(
        blank=True, null=True, default=0, verbose_name='จำนวนที่ไม่ชอบ')
    published_at = models.DateField(verbose_name=u'วันที่ประกาศ')
    published = models.BooleanField(choices=[(False, 'ร่าง'), (
        True, 'เผยแพร่')], blank=True, null=True, default=False, verbose_name=u'เผยแพร่')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลประชาสัมพันธ์'
        db_table = "tbt_webboards"


class Comment(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(
        Post, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=u'หัวข้อ/เรื่อง')
    comment_by = models.OneToOneField(
        Profile, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=u'แสดงความคิดเห็นโดย', editable=False)
    descriptions = RichTextField(verbose_name=u'รายละเอียด/ข้อมูลเพิ่มเติม')
    total_like = models.IntegerField(
        blank=True, null=True, default=0, verbose_name='จำนวนที่ชอบ')
    total_dislike = models.IntegerField(
        blank=True, null=True, default=0, verbose_name='จำนวนที่ไม่ชอบ')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลแสดงความคิดเห็น'
        db_table = "tbt_comments"


class Reply(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(
        Comment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=u'หัวข้อ/เรื่อง')
    reply_by = models.OneToOneField(
        Profile, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=u'ตอบกลับโดย', editable=False)
    descriptions = RichTextField(verbose_name=u'รายละเอียด/ข้อมูลเพิ่มเติม')
    total_like = models.IntegerField(
        blank=True, null=True, default=0, verbose_name='จำนวนที่ชอบ')
    total_dislike = models.IntegerField(
        blank=True, null=True, default=0, verbose_name='จำนวนที่ไม่ชอบ')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลตอบกลับความคิดเห็น'
        db_table = "tbt_replys"
