# Generated by Django 5.0 on 2024-03-15 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreAPI', '0005_alter_answers_options_alter_questions_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='prefix_question',
            field=models.TextField(blank=True, default=None, verbose_name='پیش متن سوال'),
        ),
    ]