from django.db import models
import uuid
from employee.models import Profile
from master.models import STATUS_CHOICES, Position

# Create your models here.
CHOICES_IDLE = [(False, 'ว่าง'), (True, 'ไม่ว่าง')]
CHOICES_TRAINED = [(False, 'ยัง'), (True, 'เรียบร้อย')]
CHOICES_ASWER = [(False, 'ไม่ถูก'), (True, 'ถูก')]


class TrainingRoom(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(
        max_length=255, unique=True, verbose_name=u'หัวข้อ')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    total_per_room = models.IntegerField(
        blank=True, null=True, default=0, verbose_name=u'จำนวนคน/ห้อง')
    is_idle = models.BooleanField(
        blank=True, null=True, default=False, choices=CHOICES_IDLE, verbose_name=u'การใช้งาน')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลห้องอบรม'
        db_table = "tbt_trainingrooms"


class Trainer(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    company = models.CharField(
        max_length=255, unique=True, verbose_name=u'บริษัท')
    position = models.OneToOneField(
        Position, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=u'ตำแหน่ง')
    email = models.CharField(
        max_length=255, unique=True, verbose_name=u'ที่อยู่อีเมล์')
    telno = models.CharField(
        max_length=255, unique=True, verbose_name=u'เบอร์โทรศัพท์')
    mobileno = models.CharField(
        max_length=255, unique=True, verbose_name=u'เบอร์โทรศัพท์มือถือ')
    avatar = models.CharField(
        max_length=255, unique=True, verbose_name=u'รูปประจำตัว')
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลวิทยากร'
        db_table = "tbt_trainers"


class Training(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    room_id = models.OneToOneField(
        TrainingRoom, on_delete=models.CASCADE, verbose_name="ห้องที่อบรม")
    subject = models.CharField(
        max_length=255, verbose_name=u'หัวข้อการอบรม')
    on_date = models.DateField(verbose_name=u'วันที่อบรม')
    from_time = models.TimeField(verbose_name=u'เวลา/เริ่ม')
    to_time = models.TimeField(verbose_name=u'เวลา/ถึง')
    trainer_id = models.OneToOneField(
        Trainer, on_delete=models.CASCADE, verbose_name="วิทยากร")
    descriptions = models.TextField(blank=True, verbose_name=u'รายละเอียด')
    is_complete = models.BooleanField(
        blank=True, choices=CHOICES_TRAINED, default=False, verbose_name=u'อบรมแล้ว')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลการอบรม'
        db_table = "tbt_trainings"


class ImagesTraining(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    training_id = models.ForeignKey(
        Training, on_delete=models.CASCADE, verbose_name=u'หัวข้อ')
    image = models.FileField(verbose_name=u'รูปประกอบ')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลรูปภาพประกอบการอบรม'
        db_table = "tbt_imagetrainings"


class TrainingDetail(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    training_id = models.OneToOneField(
        Training, on_delete=models.CASCADE, verbose_name="หัวข้อมที่อบรม")
    profile_id = models.OneToOneField(
        Profile, on_delete=models.CASCADE, verbose_name="ชื่อพนักงาน")
    on_date = models.DateTimeField(
        blank=True, null=True, verbose_name=u'วันที่ทำการอบรม')
    training_score = models.DecimalField(
        blank=True, decimal_places=18, max_digits=44, verbose_name=u'คะแนนที่ได้')
    descriptions = models.TextField(
        blank=True, verbose_name=u'รายละเอียด/เสนอแนะ')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลพนักงานที่เข้าอบรม'
        db_table = "tbt_trainingdetail"


class Squize(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    training_id = models.ForeignKey(
        Training, on_delete=models.CASCADE, verbose_name="หัวข้ออบรม")
    title = models.CharField(max_length=255, verbose_name=u'หัวข้อ')
    descriptions = models.TextField(
        blank=True, verbose_name=u'รายละเอียด/เสนอแนะ')
    score_length = models.DecimalField(
        decimal_places=18, max_digits=44, verbose_name=u'คะแนนเต็ม')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลแบบทดสอบหลังการอบรม'
        db_table = "tbt_squizes"


class ImagesSquize(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    squize_id = models.ForeignKey(
        Squize, on_delete=models.CASCADE, verbose_name=u'หัวข้อ')
    image = models.ImageField(null=True, blank=True, verbose_name=u'รูปประกอบ')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลรูปภาพประกอบการอบรม'
        db_table = "tbt_illustrationtrainings"


class SquizeDetail(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    training_id = models.ForeignKey(
        Squize, on_delete=models.CASCADE, verbose_name="แบบทดสอบ")
    title = models.CharField(max_length=255, verbose_name=u'คำถาม')
    descriptions = models.TextField(
        blank=True, verbose_name=u'รายละเอียด')
    score_length = models.DecimalField(blank=True, null=True, default=0,
                                       decimal_places=18, max_digits=44, verbose_name=u'คะแนนเต็ม')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลแบบทดสอบหลังการอบรม/ข้อสอบ'
        db_table = "tbt_squizedetails"


class SquizeChoice(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    training_id = models.ForeignKey(
        SquizeDetail, on_delete=models.CASCADE, verbose_name="คำถาม")
    title = models.CharField(max_length=255, verbose_name=u'คำตอบ')
    descriptions = models.TextField(
        blank=True, verbose_name=u'รายละเอียด')
    score_length = models.DecimalField(blank=True, null=True, default=0,
                                       decimal_places=18, max_digits=44, verbose_name=u'คะแนนเต็ม')
    is_answer = models.BooleanField(
        choices=CHOICES_ASWER, default=False, verbose_name=u'เฉลย/คำตอบ')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลแบบทดสอบหลังการอบรม/คำตอบ'
        db_table = "tbt_squizechoices"


class EmployeeTester(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    training_id = models.OneToOneField(
        Training, on_delete=models.CASCADE, verbose_name=u'หัวข้อการอบรม')
    profile_id = models.OneToOneField(
        Profile, on_delete=models.CASCADE, verbose_name=u'ผู้ทำการทดสอบ')
    on_round = models.IntegerField(
        null=True, blank=True, default=1, verbose_name=u'รอบที่สอบ')
    on_date = models.DateTimeField(verbose_name=u'วันที่ทดสอบ')
    score = models.DecimalField(
        null=True, decimal_places=18, max_digits=44, default=0, verbose_name=u'คะแนนนที่ได้')
    descriptions = models.TextField(
        blank=True, verbose_name=u'รายละเอียด')
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลผลการทดสอบหลังการอบรม'
        db_table = "tbt_aftertrainings"


class EmployeeTesterDetail(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False)
    profile_id = models.OneToOneField(
        EmployeeTester, on_delete=models.CASCADE, verbose_name="หัวข้อการอบรม")
    squize_id = models.OneToOneField(
        SquizeDetail, on_delete=models.CASCADE, verbose_name="คำถาม")
    answer_id = models.OneToOneField(
        SquizeChoice, on_delete=models.CASCADE, verbose_name="คำตอบ")
    active = models.BooleanField(
        choices=STATUS_CHOICES, default=False, verbose_name=u'สถานะ')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=u'สร้างเมื่อ', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=u'แก้ไขเมื่อ')

    class Meta:
        # abstract = True
        verbose_name_plural = u'ข้อมูลผลการทดสอบหลังการอบรม/คำตอบ'
        db_table = "tbt_aftertrainingdetails"
