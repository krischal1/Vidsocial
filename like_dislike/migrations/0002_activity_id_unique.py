# Generated by Django 2.1.2 on 2018-11-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like_dislike', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='id_unique',
            field=models.IntegerField(default=1, unique=True),
        ),
    ]
