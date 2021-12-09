# Generated by Django 4.0 on 2021-12-09 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('leave', '0001_initial'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='leave_type_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.leavetype', verbose_name='ประเภทที่ลา'),
        ),
        migrations.AddField(
            model_name='leave',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.profile', verbose_name='ชื่อพนักงาน'),
        ),
        migrations.AddField(
            model_name='attachmentleave',
            name='leave_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.leave', verbose_name='หัวข้อการลา'),
        ),
    ]
