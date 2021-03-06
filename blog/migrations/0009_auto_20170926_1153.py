# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 02:53
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170916_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='포스팅 제목을 입력해주세요. 최대 100자 내외', max_length=100, validators=[blog.models.min_length_3_validator], verbose_name='제목'),
        ),
    ]
