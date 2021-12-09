# Generated by Django 4.0 on 2021-12-09 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('accident', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='approveaccident',
            name='profile_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.profile', verbose_name='ผู้รับเรื่อง'),
        ),
        migrations.AddField(
            model_name='accident',
            name='accident_group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accident.accidentgroup', verbose_name='ประเภทของอุบัติเหติ'),
        ),
        migrations.AddField(
            model_name='accident',
            name='profile_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.profile', verbose_name='ผู้ที่ทำให้เกิอุบัติเหตุ'),
        ),
    ]
