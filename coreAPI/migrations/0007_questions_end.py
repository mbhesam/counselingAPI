# Generated by Django 5.0 on 2024-03-15 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreAPI', '0006_alter_questions_prefix_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='end',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
