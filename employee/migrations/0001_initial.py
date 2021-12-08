# Generated by Django 4.0 on 2021-12-08 08:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permision',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('09368ec0-37ba-4924-b5d3-bfa64874ed3a'), editable=False, primary_key=True, serialize=False)),
                ('descriptions', models.TextField(blank=True, verbose_name='รายละเอียด')),
                ('is_admin', models.BooleanField(choices=[(False, 'ไม่'), (True, 'ใช่')], default=False, verbose_name='ผู้ดูแลระบบ')),
                ('is_approve', models.BooleanField(choices=[(False, 'ไม่'), (True, 'ใช่')], default=False, verbose_name='การอนุมัติ')),
                ('is_edit', models.BooleanField(choices=[(False, 'ไม่'), (True, 'ใช่')], default=False, verbose_name='สามารถแก้ไขข้อมูล')),
                ('is_create', models.BooleanField(choices=[(False, 'ไม่'), (True, 'ใช่')], default=False, verbose_name='สามารถสร้างข้อมูลใหม่')),
                ('is_delete', models.BooleanField(choices=[(False, 'ไม่'), (True, 'ใช่')], default=False, verbose_name='สามารถลบข้อมูล')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลสิทธฺ์การใช้งาน',
                'db_table': 'tbt_permisions',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('404378a3-5036-42fc-b964-4df66e293720'), editable=False, primary_key=True, serialize=False)),
                ('empcode', models.CharField(max_length=25, unique=True, verbose_name='รหัสพนักงาน')),
                ('description', models.TextField(blank=True, verbose_name='รายละเอียด/เพิ่มเติม')),
                ('address_1', models.CharField(blank=True, max_length=25, verbose_name='ที่อยู่ 1')),
                ('address_2', models.CharField(blank=True, max_length=25, verbose_name='ที่อยู่ 2')),
                ('mobile_no', models.CharField(blank=True, max_length=25, verbose_name='เบอร์โทรศัพท์มือถือ')),
                ('tel_no', models.CharField(blank=True, max_length=25, verbose_name='เบอร์โทรศัพท์')),
                ('employee_date', models.DateField(blank=True, null=True, verbose_name='วันเริ่มงาน')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='วันเกิด')),
                ('status', models.CharField(blank=True, choices=[('-', 'ไม่ระบุ'), ('S', 'โสด'), ('M', 'สมรส')], max_length=5, null=True, verbose_name='สถานะภาพ')),
                ('spouse_name', models.CharField(blank=True, max_length=255, verbose_name='คู่สมรส')),
                ('child', models.IntegerField(blank=True, verbose_name='จำนวนบุตร')),
                ('driver_car', models.BooleanField(blank=True, choices=[(False, 'ไม่'), (True, 'ใช่')], default=False, verbose_name='สามารถขับรถยนต์ได้')),
                ('driver_license_car', models.BooleanField(blank=True, choices=[(False, 'ไม่มี'), (True, 'มี')], default=False, verbose_name='มีใบขับขี่รถยนต์')),
                ('driver_moto', models.BooleanField(blank=True, choices=[(False, 'ไม่'), (True, 'ใช่')], default=False, verbose_name='สามารถขับจักรยานยนต์ได้')),
                ('driver_license_moto', models.BooleanField(blank=True, choices=[(False, 'ไม่มี'), (True, 'มี')], default=False, verbose_name='มีใบขับขี่จักรยานยนต์')),
                ('driver_floklift', models.BooleanField(blank=True, choices=[(False, 'ไม่'), (True, 'ใช่')], default=False, verbose_name='สามารถขับ Floklift ได้')),
                ('driver_license_floklift', models.BooleanField(blank=True, choices=[(False, 'ไม่มี'), (True, 'มี')], default=False, verbose_name='มีใบขับขี่ Floklift')),
                ('contact_name', models.CharField(blank=True, max_length=255, verbose_name='ชื่อผู้ติดต่อ')),
                ('contact_mobileno', models.CharField(blank=True, max_length=255, verbose_name='เบอร์โทรผู้ติดต่อ')),
                ('is_militaried', models.BooleanField(blank=True, choices=[(False, 'ไม่'), (True, 'ใช่')], default=False, verbose_name='ผ่านการเกณต์ทหารแล้ว')),
                ('business_leave', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ลากิจ')),
                ('vacation_leave', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ลาพักร้อน')),
                ('military_leave', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ลาเกณฑ์ทหาร')),
                ('child_birth_leave', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ลาคลอด')),
                ('priesthood_leave', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ลาบวช')),
                ('sick_leave', models.DecimalField(decimal_places=18, default=30, max_digits=44, null=True, verbose_name='ลาป่วย')),
                ('overleave_business', models.DecimalField(decimal_places=18, default=30, max_digits=44, null=True, verbose_name='ลากิจเกิน')),
                ('overleave_priesthood', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ลาบวชเกิน')),
                ('overleave_sick', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ลาป่วยเกิน')),
                ('overleave_military', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ลาเกณฑ์ทหารเกิน')),
                ('birth_day_leave', models.DecimalField(decimal_places=18, default=1, max_digits=44, null=True, verbose_name='ลาวันเกิด')),
                ('married_leave', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ลาจดทะเบียนสมรส')),
                ('salary', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='เงินเดือน')),
                ('avatar', models.FileField(blank=True, null=True, upload_to='', verbose_name='รูปประจำตัว')),
                ('signature', models.FileField(blank=True, null=True, upload_to='', verbose_name='ลายเซนต์')),
                ('is_passed', models.CharField(choices=[('-', 'ยังไม่ผ่านการประเมิน'), ('P', 'ผ่านการประเมินเรียบร้อยแล้ว'), ('R', 'พ้นจากเป็นพนักงาน')], default='-', max_length=1, verbose_name='สถานะการทำงาน')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลผู้ใช้งาน',
                'db_table': 'tbt_profiles',
            },
        ),
    ]
