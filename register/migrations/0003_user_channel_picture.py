# Generated by Django 2.1.2 on 2018-11-22 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20181122_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='channel_picture',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
