# Generated by Django 4.0 on 2021-12-09 02:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('99b756ad-c68d-4695-9ddc-54144b5c92a2'), editable=False, primary_key=True, serialize=False)),
                ('district', models.CharField(max_length=255, unique=True, verbose_name='ชื่อ')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, verbose_name='รายละเอียด')),
                ('latitude', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ละติจูด')),
                ('longitude', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ลองจิจูด')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลอำเภอ',
                'db_table': 'tbt_districts',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('63e6b904-342a-4a09-bca7-a8cec5e7c936'), editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='รหัส')),
                ('province', models.CharField(max_length=255, unique=True, verbose_name='ชื่อ')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, verbose_name='รายละเอียด')),
                ('latitude', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ละติจูด')),
                ('longitude', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ลองจิจูด')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลจังหวัด',
                'db_table': 'tbt_provinces',
            },
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('bdde6bf4-3b5f-44e8-a67f-daac34b2bb23'), editable=False, primary_key=True, serialize=False)),
                ('zipcode', models.CharField(max_length=10, verbose_name='รหัสไปรษณีย์')),
                ('tombon', models.CharField(max_length=255, verbose_name='ตำบล')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, verbose_name='รายละเอียด')),
                ('latitude', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ละติจูด')),
                ('longitude', models.DecimalField(decimal_places=18, default=0, max_digits=44, null=True, verbose_name='ลองจิจูด')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
                ('district_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='regional.district', verbose_name='จังหวัด')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลรหัสไปรษณีย์',
                'db_table': 'tbt_zipcodes',
            },
        ),
        migrations.AddField(
            model_name='district',
            name='province_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='regional.province', verbose_name='จังหวัด'),
        ),
    ]