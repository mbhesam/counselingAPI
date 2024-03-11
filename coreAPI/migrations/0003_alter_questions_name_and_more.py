# Generated by Django 5.0 on 2024-03-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreAPI', '0002_questions_remove_subcategory_category_answers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام سوال'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='original_question',
            field=models.TextField(default=None, verbose_name='متن اصلی سوال'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='prefix_question',
            field=models.TextField(default=None, verbose_name='پیش متن سوال'),
        ),
    ]
