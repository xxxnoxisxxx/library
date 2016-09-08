# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-08 18:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20160908_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 8, 18, 21, 53, 449736, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 18, 21, 53, 449762, tzinfo=utc)),
        ),
    ]
