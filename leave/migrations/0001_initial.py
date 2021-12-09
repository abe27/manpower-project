# Generated by Django 4.0 on 2021-12-09 02:58

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentLeave',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('6c51c883-fa8c-424b-8dac-4ce77fc48aa0'), editable=False, primary_key=True, serialize=False)),
                ('attachment', models.FileField(upload_to='', verbose_name='เอกสารประกอบการลา')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
            ],
            options={
                'verbose_name_plural': 'บันทึกข้อมูลเอกสารประกอบการลา',
                'db_table': 'tbt_attachmentleaves',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('df22b04f-2c5b-43e5-a7fc-4768871e7a56'), editable=False, primary_key=True, serialize=False)),
                ('leave_on', models.DateField(verbose_name='วันที่ลา')),
                ('from_time', models.TimeField(verbose_name='เริ่มจากเวลา')),
                ('to_time', models.TimeField(verbose_name='ถึงเวลา')),
                ('reason', models.TextField(verbose_name='สาเหตุที่ลา/เหตุผล')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, default='-', null=True, verbose_name='ข้อมูลเพิ่มเติม')),
                ('total_leave', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ผลรวม')),
                ('leader_approve', models.IntegerField(blank=True, choices=[(0, '-'), (1, 'Reject'), (2, 'Approved')], null=True, verbose_name='หัวหน้างาน/สถานะ')),
                ('leader_approve_at', models.DateField(blank=True, null=True, verbose_name='หัวหน้า/อัพเดทข้อมูลเมื่อ')),
                ('leader_comment', models.TextField(blank=True, null=True, verbose_name='หัวหน้า/ข้อมูลเพิ่มเติม')),
                ('mgr_approve', models.IntegerField(blank=True, choices=[(0, '-'), (1, 'Reject'), (2, 'Approved')], null=True, verbose_name=' ผู้จัดการ/สถานะ')),
                ('mgr_approve_at', models.DateField(blank=True, null=True, verbose_name='ผู้จัดการ/อัพเดทข้อมูลเมื่อ')),
                ('mgr_comment', models.TextField(blank=True, null=True, verbose_name='ผู้จัดการ/ข้อมูลเพิ่มเติม')),
                ('hr_approve', models.IntegerField(blank=True, choices=[(0, '-'), (1, 'Reject'), (2, 'Approved')], null=True, verbose_name='พนักงานทัพยากรบุคคล/สถานะ')),
                ('hr_approve_at', models.DateField(blank=True, null=True, verbose_name='พนักงานทัพยากรบุคคล/อัพเดทข้อมูลเมื่อ')),
                ('hr_comment', models.TextField(blank=True, null=True, verbose_name='พนักงานทัพยากรบุคคล/ข้อมูลเพิ่มเติม')),
                ('sendmail', models.BooleanField(choices=[(False, 'ยังไม่ส่ง'), (True, 'ส่งแล้ว')], default=False, verbose_name='สถานะการส่งเมล์')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
            ],
            options={
                'verbose_name_plural': 'บันทึกข้อมูลการลา',
                'db_table': 'tbt_leaves',
            },
        ),
    ]