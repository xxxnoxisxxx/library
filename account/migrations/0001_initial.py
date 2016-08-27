# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-27 14:34
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.CharField(max_length=9, unique=True)),
                ('mobile', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('loans', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Loan')),
                ('reader', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reservation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Reservation')),
            ],
            options={
                'db_table': 'reader',
            },
        ),
    ]
