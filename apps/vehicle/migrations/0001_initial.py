# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('car', 'Car'), ('bikes', 'Bikes'), ('trucks', 'Trucks'), ('other', 'Other')], default='male', max_length=10)),
            ],
        ),
    ]
