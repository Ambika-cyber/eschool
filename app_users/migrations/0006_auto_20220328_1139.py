# Generated by Django 3.1.1 on 2022-03-28 06:09

import app_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_auto_20220328_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=app_users.models.path_and_rename, verbose_name='Profile Picture'),
        ),
    ]
