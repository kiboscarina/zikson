# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20171010_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hedline', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('picture', models.FileField(blank=True, null=True, upload_to='news_pic')),
            ],
        ),
    ]
