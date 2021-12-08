from django.db import models
import uuid

STATUS_CHOICES = [
    (False, 'ปิด'),
    (True, 'เปิด')
]

STATUS_APPROVE_CHOICES = [
    (False, 'ไม่'),
    (True, 'ใช่')
]

STATUS_EXPLOIT_CHOICES = [
    (False, 'ไม่มี'),
    (True, 'มี')
]

# Create your models here.


class Whs(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลคลังสินค้า'
        db_table = "tbt_whs"


class Position(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลตำแหน่ง'
        db_table = "tbt_positions"


class Section(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลสาขา/หน่วยงาน'
        db_table = "tbt_sections"


class Department(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลแผนก'
        db_table = "tbt_departments"


class Shift(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')  # A/B/S
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    time_attendance = models.DecimalField(null=True,
                                          decimal_places=18,
                                          max_digits=44, default=8, verbose_name=u'เวลาทำงาน(ชม.)')
    fee_per = models.DecimalField(null=True,
                                  decimal_places=18,
                                  max_digits=44, default=0, verbose_name=u'ค่ากะ(บาท)')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลการเข้างาน'
        db_table = "tbt_shiftments"


class Organization(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'องค์กร')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    mail_to = models.CharField(max_length=255, verbose_name=u'เมล์ TO')
    mail_cc = models.CharField(max_length=255, verbose_name=u'เมล์ CC')
    mail_bc = models.CharField(max_length=255, verbose_name=u'เมล์ BC')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลองค์กร'
        db_table = "tbt_organizations"


class Educationals(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลระดับการศึกษา'
        db_table = "tbt_educationals"


class LeaveType(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลประเภทการลา'
        db_table = "tbt_leavegroups"


class CompanyCalendar(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    on_date = models.DateField(verbose_name=u'วันที่')
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลปฏิทินวันหยุดของบริษัท'
        db_table = "tbt_companycalendars"


class Categories(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลหมวดหมู่ข่าวสาร'
        db_table = "tbt_categories"
