# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-31 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20180130_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, default='no-img.jpg', null=True, upload_to='profile/picture/'),
        ),
    ]
