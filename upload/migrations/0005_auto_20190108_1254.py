# Generated by Django 2.1.3 on 2019-01-08 12:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_video_monetize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default={}, null=True, size=None),
        ),
    ]