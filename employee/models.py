from django.db import models
from django.contrib.auth.models import User
import uuid

from master.models import STATUS_APPROVE_CHOICES, STATUS_CHOICES, STATUS_EXPLOIT_CHOICES, Department, Educationals, Organization, Position, Section, Shift
from regional.models import ZipCode


# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    user_id = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=u'ผู้ใช้งาน')
    zipcode_id = models.OneToOneField(
        ZipCode, on_delete=models.CASCADE, verbose_name=u'รหัสไปรษณีย์')
    position_id = models.OneToOneField(
        Position, on_delete=models.CASCADE, verbose_name=u'ตำแหน่ง')
    section_id = models.OneToOneField(
        Section, on_delete=models.CASCADE, verbose_name=u'สาขา/หน่วยงาน')
    department_id = models.OneToOneField(
        Department, on_delete=models.CASCADE, verbose_name=u'แผนก')
    shift_id = models.OneToOneField(
        Shift, on_delete=models.CASCADE, verbose_name=u'ข้อมูลเข้างาน')
    organiz_id = models.OneToOneField(
        Organization, on_delete=models.CASCADE, verbose_name=u'องค์กร/หัวหน้างาน')
    edu_id = models.OneToOneField(
        Educationals, on_delete=models.CASCADE, verbose_name=u'ระดับการศึกษา')
    empcode = models.CharField(
        max_length=25, unique=True, verbose_name=u'รหัสพนักงาน')
    description = models.TextField(
        blank=True, verbose_name=u'รายละเอียด/เพิ่มเติม')
    address_1 = models.CharField(
        max_length=25, blank=True, verbose_name=u'ที่อยู่ 1')
    address_2 = models.CharField(
        max_length=25, blank=True, verbose_name=u'ที่อยู่ 2')
    mobile_no = models.CharField(
        max_length=25, blank=True, verbose_name=u'เบอร์โทรศัพท์มือถือ')
    tel_no = models.CharField(
        max_length=25, blank=True, verbose_name=u'เบอร์โทรศัพท์')
    employee_date = models.DateField(
        blank=True, null=True, verbose_name=u'วันเริ่มงาน')
    birthdate = models.DateField(
        blank=True, null=True, verbose_name=u'วันเกิด')
    status = models.CharField(max_length=5, blank=True, null=True, choices=[(
        '-', 'ไม่ระบุ'), ('S', 'โสด'), ('M', 'สมรส')], verbose_name=u'สถานะภาพ')
    spouse_name = models.CharField(
        blank=True, max_length=255, verbose_name=u'คู่สมรส')
    child = models.IntegerField(blank=True, verbose_name=u'จำนวนบุตร')
    driver_car = models.BooleanField(
        blank=True, default=False, choices=STATUS_APPROVE_CHOICES, verbose_name=u'สามารถขับรถยนต์ได้')
    driver_license_car = models.BooleanField(
        blank=True, default=False, choices=STATUS_EXPLOIT_CHOICES, verbose_name=u'มีใบขับขี่รถยนต์')
    driver_moto = models.BooleanField(
        blank=True, default=False, choices=STATUS_APPROVE_CHOICES, verbose_name=u'สามารถขับจักรยานยนต์ได้')
    driver_license_moto = models.BooleanField(
        blank=True, default=False, choices=STATUS_EXPLOIT_CHOICES, verbose_name=u'มีใบขับขี่จักรยานยนต์')

    driver_floklift = models.BooleanField(
        blank=True, default=False, choices=STATUS_APPROVE_CHOICES, verbose_name=u'สามารถขับ Floklift ได้')
    driver_license_floklift = models.BooleanField(
        blank=True, default=False, choices=STATUS_EXPLOIT_CHOICES, verbose_name=u'มีใบขับขี่ Floklift')
    contact_name = models.CharField(
        max_length=255, blank=True, verbose_name=u'ชื่อผู้ติดต่อ')
    contact_mobileno = models.CharField(
        max_length=255, blank=True, verbose_name=u'เบอร์โทรผู้ติดต่อ')
    is_militaried = models.BooleanField(
        choices=STATUS_APPROVE_CHOICES, blank=True, default=False, verbose_name=u'ผ่านการเกณต์ทหารแล้ว')
    business_leave = models.DecimalField(null=True,
                                         decimal_places=18,
                                         max_digits=44, default=0, verbose_name=u'ลากิจ')
    vacation_leave = models.DecimalField(null=True,
                                         decimal_places=18,
                                         max_digits=44, default=0, verbose_name=u'ลาพักร้อน')
    military_leave = models.DecimalField(null=True,
                                         decimal_places=18,
                                         max_digits=44, default=0, verbose_name=u'ลาเกณฑ์ทหาร')
    child_birth_leave = models.DecimalField(null=True,
                                            decimal_places=18,
                                            max_digits=44, default=0, verbose_name=u'ลาคลอด')
    priesthood_leave = models.DecimalField(null=True,
                                           decimal_places=18,
                                           max_digits=44, default=0, verbose_name=u'ลาบวช')
    sick_leave = models.DecimalField(null=True,
                                     decimal_places=18,
                                     max_digits=44, default=30, verbose_name=u'ลาป่วย')
    # #####
    overleave_business = models.DecimalField(null=True,
                                             decimal_places=18,
                                             max_digits=44, default=30, verbose_name=u'ลากิจเกิน')
    overleave_priesthood = models.DecimalField(null=True,
                                               decimal_places=18,
                                               max_digits=44, default=0, verbose_name=u'ลาบวชเกิน')
    overleave_sick = models.DecimalField(null=True,
                                         decimal_places=18,
                                         max_digits=44, default=0, verbose_name=u'ลาป่วยเกิน')
    overleave_military = models.DecimalField(null=True,
                                             decimal_places=18,
                                             max_digits=44, default=0, verbose_name=u'ลาเกณฑ์ทหารเกิน')
    birth_day_leave = models.DecimalField(null=True,
                                          decimal_places=18,
                                          max_digits=44, default=1, verbose_name=u'ลาวันเกิด')
    married_leave = models.DecimalField(null=True,
                                        decimal_places=18,
                                        max_digits=44, default=0, verbose_name=u'ลาจดทะเบียนสมรส')
    # #####
    salary = models.DecimalField(null=True,
                                 decimal_places=18,
                                 max_digits=44, default=0, verbose_name=u'เงินเดิน')
    avatar = models.FileField(blank=True, null=True,
                              verbose_name=u'รูปประจำตัว')
    signature = models.FileField(
        blank=True, null=True, verbose_name=u'ลายเซนต์')

    is_passed = models.BooleanField(
        choices=[(False, 'ยังไม่ผ่านการประเมิน'), (True, 'ผ่านการประเมินเรียบร้อยแล้ว')], default=False, verbose_name=u'สถานะการทำงาน')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลผู้ใช้งาน'
        db_table = "tbt_profiles"


class Permision(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    user_id = models.OneToOneField(
        Profile, on_delete=models.CASCADE, verbose_name=u'ผู้ใช้งาน')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    is_admin = models.BooleanField(
        choices=STATUS_APPROVE_CHOICES, default=False, verbose_name=u'ผู้ดูแลระบบ')
    is_approve = models.BooleanField(
        choices=STATUS_APPROVE_CHOICES, default=False, verbose_name=u'การอนุมัติ')
    is_edit = models.BooleanField(
        choices=STATUS_APPROVE_CHOICES, default=False, verbose_name=u'สามารถแก้ไขข้อมูล')
    is_create = models.BooleanField(
        choices=STATUS_APPROVE_CHOICES, default=False, verbose_name=u'สามารถสร้างข้อมูลใหม่')
    is_delete = models.BooleanField(
        choices=STATUS_APPROVE_CHOICES, default=False, verbose_name=u'สามารถลบข้อมูล')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลสิทธฺ์การใช้งาน'
        db_table = "tbt_permisions"
