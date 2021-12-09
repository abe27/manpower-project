# Generated by Django 4.0 on 2021-12-09 02:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeAttendModel',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('bde2af2e-be69-4d8a-93ee-89443d1cf2f9'), editable=False, primary_key=True, serialize=False)),
                ('record_in', models.DateTimeField(blank=True, verbose_name='เข้าที่ทำงานเมื่อ')),
                ('record_out', models.DateTimeField(blank=True, verbose_name='ออกจากที่ทำงานเมื่อ')),
                ('is_change_shift', models.BooleanField(blank=True, choices=[(False, 'ไม่'), (True, 'ใช่')], default=False, verbose_name='เปลี่ยนกะ')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, verbose_name='ข้อมูลเพิ่มเติม')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.profile', verbose_name='พนักงาน')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลบันทึกเวลาเข้าทำงาน',
                'db_table': 'tbt_timeattendances',
            },
        ),
        migrations.CreateModel(
            name='ImageTimeAttendance',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('30717a51-6e56-477c-a2de-bf2216ec2ac4'), editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
                ('training_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeattendance.timeattendmodel', verbose_name='หัวข้อ')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลรูปภาพประกอบบันทึกเวลาเข้าทำงาน',
                'db_table': 'tbt_imagetimeattendances',
            },
        ),
    ]
