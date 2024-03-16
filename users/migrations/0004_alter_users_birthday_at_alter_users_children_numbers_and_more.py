# Generated by Django 5.0 on 2024-03-16 11:23

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='birthday_at',
            field=django_jalali.db.models.jDateTimeField(verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='users',
            name='children_numbers',
            field=models.IntegerField(verbose_name='تعداد فرزندان'),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='ساخته شده در زمان'),
        ),
        migrations.AlterField(
            model_name='users',
            name='father_name',
            field=models.CharField(max_length=100, verbose_name='نام پدر'),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('مرد', 'مرد'), ('زن', 'زن')], max_length=5, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='users',
            name='marriage_history',
            field=models.IntegerField(verbose_name='سابقه تاهل'),
        ),
        migrations.AlterField(
            model_name='users',
            name='married',
            field=models.CharField(choices=[('مجرد', 'مجرد'), ('متاهل', 'متاهل')], max_length=8, verbose_name='متاهل'),
        ),
        migrations.AlterField(
            model_name='users',
            name='mother_name',
            field=models.CharField(max_length=100, verbose_name='نام مادر'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=11, verbose_name='شماره تلفن همراه'),
        ),
        migrations.AlterField(
            model_name='users',
            name='platform',
            field=models.CharField(max_length=20, verbose_name='پلتفرم پاسخ گویی ربات'),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=200, unique=True, verbose_name='آی دی'),
        ),
    ]
