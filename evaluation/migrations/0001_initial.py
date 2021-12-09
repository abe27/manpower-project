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
            name='Evaluated',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('98fdb7db-e492-46db-93a0-9fcef952936b'), editable=False, primary_key=True, serialize=False)),
                ('evaluate_date', models.DateTimeField(blank=True, null=True, verbose_name='วันที่ประเมิน')),
                ('evaluate_score', models.DecimalField(blank=True, decimal_places=18, default=0, max_digits=44, null=True, verbose_name='คะแนนที่ได้')),
                ('evaluate_status', models.CharField(blank=True, choices=[('-', '-'), ('N', 'ไม่ผ่าน'), ('P', 'ผ่าน')], max_length=1, null=True, verbose_name='สถานะ')),
                ('evaluate_comment', models.TextField(blank=True, null=True, verbose_name='ข้อเสนอแนะ')),
                ('is_accept', models.CharField(blank=True, choices=[('-', '-'), ('N', 'ไม่ยอรับ'), ('A', 'ยอมรับ')], max_length=1, null=True, verbose_name='การยอมรับ')),
                ('is_not_accept', models.TextField(blank=True, null=True, verbose_name='ข้อเสนอแนะ/กรณีไม่ยอมรับ/เหตุผลอื่นๆ')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลพนักงานที่ทำการประเมินเสร็จแล้ว',
                'db_table': 'tbt_evaluateds',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('538313a9-92e1-4260-860d-89cbfc3b2fe2'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='หัวข้อ')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, verbose_name='รายละเอียด')),
                ('score', models.DecimalField(blank=True, decimal_places=18, default=0.0, max_digits=44, verbose_name='คะแนนเต็ม')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลการประเมิน',
                'db_table': 'tbt_evaluations',
            },
        ),
        migrations.CreateModel(
            name='EvaluationGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('cc302d1a-94a2-4616-8824-1ebc201a9d00'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='หัวข้อ')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, verbose_name='รายละเอียด')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลประเภทการประเมิน',
                'db_table': 'tbt_evaluationgroups',
            },
        ),
        migrations.CreateModel(
            name='EvaluationLength',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('de1b9b9f-16c4-4900-841b-61588fecce5f'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='หัวข้อ')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, verbose_name='รายละเอียด')),
                ('score', models.DecimalField(blank=True, decimal_places=18, default=0.0, max_digits=44, verbose_name='ช่วงคะแนน')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
                ('evaluate_group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='evaluation.evaluationgroup', verbose_name='ประเภทการการประเมิน')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลช่องคะแนนการประเมิน',
                'db_table': 'tbt_evaluationlengths',
            },
        ),
        migrations.CreateModel(
            name='EvaluationDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('1d9145f6-3dac-4b28-9e9c-5dae31f0b196'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='หัวข้อ')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, verbose_name='รายละเอียด')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
                ('evaluate_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='evaluation.evaluation', verbose_name='หัวข้อการประเมิน')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลการประเมินเพิ่มเติม',
                'db_table': 'tbt_evaluationdetails',
            },
        ),
        migrations.AddField(
            model_name='evaluation',
            name='evaluate_group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='evaluation.evaluationgroup', verbose_name='ประเภทการการประเมิน'),
        ),
        migrations.CreateModel(
            name='EvaluatedDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('782f95a5-44ee-4ebe-967a-508456be6f5a'), editable=False, primary_key=True, serialize=False)),
                ('remark', models.TextField(blank=True, null=True, verbose_name='ข้อเสนอแนะ')),
                ('is_accept', models.CharField(blank=True, choices=[('-', '-'), ('N', 'ไม่ยอรับ'), ('A', 'ยอมรับ')], max_length=1, null=True, verbose_name='ยอมรับ')),
                ('is_not_accept_remark', models.TextField(blank=True, null=True, verbose_name='ข้อเสนอแนะ/กรณีไม่ยอมรับ/เหตุผลอื่นๆ')),
                ('active', models.BooleanField(choices=[(False, 'ปิด'), (True, 'เปิด')], default=False, verbose_name='สถานะ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='แก้ไขเมื่อ')),
                ('evaluate_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='evaluation.evaluationdetail', verbose_name='หัวข้อการประเมิน')),
                ('profile_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='evaluation.evaluated', verbose_name='พนักงานที่ถูกประเมิน')),
                ('score_length', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='evaluation.evaluationlength', verbose_name='คะแนนที่ได้')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลพนักงานที่ทำการประเมินเพิ่มเติม',
                'db_table': 'tbt_evaluateddetails',
            },
        ),
        migrations.AddField(
            model_name='evaluated',
            name='evaluate_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='evaluation.evaluation', verbose_name='หัวข้อการประเมิน'),
        ),
        migrations.AddField(
            model_name='evaluated',
            name='profile_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.profile', verbose_name='ผู้ถูกประเมิน'),
        ),
    ]