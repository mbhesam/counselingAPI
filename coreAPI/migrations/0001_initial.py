# Generated by Django 5.0 on 2024-01-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('category', models.ManyToManyField(related_name='subcategory', to='coreAPI.category')),
            ],
        ),
        migrations.CreateModel(
            name='Advices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('category', models.ManyToManyField(related_name='advices', to='coreAPI.category')),
                ('subcategory', models.ManyToManyField(blank=True, related_name='advices', to='coreAPI.subcategory')),
            ],
        ),
    ]
