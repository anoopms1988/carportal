# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0011_roadassistance'),
        ('specification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Steering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('archived', 'Archived')], default='active', max_length=10)),
                ('turning_radius', models.CharField(max_length=20)),
                ('steering_type', models.CharField(max_length=20)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steering', to='vehicle.Variant')),
            ],
            options={
                'verbose_name_plural': 'Steering',
                'verbose_name': 'Steering',
            },
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('archived', 'Archived')], default='active', max_length=10)),
                ('wheel_size', models.CharField(max_length=20)),
                ('wheel_type', models.CharField(max_length=20)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wheel', to='vehicle.Variant')),
            ],
            options={
                'verbose_name_plural': 'Wheel',
                'verbose_name': 'Wheel',
            },
        ),
    ]
