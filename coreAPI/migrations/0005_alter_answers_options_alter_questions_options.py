# Generated by Django 5.0 on 2024-03-11 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreAPI', '0004_alter_answers_next_question_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers',
            options={'verbose_name': 'جواب', 'verbose_name_plural': 'جواب ها'},
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'verbose_name': 'سوال', 'verbose_name_plural': 'سوال ها'},
        ),
    ]
