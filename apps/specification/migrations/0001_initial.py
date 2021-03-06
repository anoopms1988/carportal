# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0010_auto_20160905_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brakes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('archived', 'Archived')], default='active', max_length=10)),
                ('rear_brakes', models.CharField(max_length=20)),
                ('front_brakes', models.CharField(max_length=20)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brakes', to='vehicle.Variant')),
            ],
            options={
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('archived', 'Archived')], default='active', max_length=10)),
                ('seating_capacity', models.CharField(max_length=20)),
                ('tank_capacity', models.CharField(max_length=20)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capacity', to='vehicle.Variant')),
            ],
            options={
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('archived', 'Archived')], default='active', max_length=10)),
                ('length', models.CharField(max_length=20)),
                ('width', models.CharField(max_length=20)),
                ('height', models.CharField(blank=True, max_length=20, null=True)),
                ('wheelbase', models.CharField(blank=True, max_length=20, null=True)),
                ('bootspace', models.CharField(blank=True, max_length=20, null=True)),
                ('kerbweight', models.CharField(blank=True, max_length=20, null=True)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimensions', to='vehicle.Variant')),
            ],
            options={
                'verbose_name_plural': 'Dimensions',
                'verbose_name': 'Dimension',
            },
        ),
        migrations.CreateModel(
            name='Engines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('archived', 'Archived')], default='active', max_length=10)),
                ('torque', models.CharField(max_length=20)),
                ('displacement', models.CharField(max_length=20)),
                ('power', models.CharField(max_length=20)),
                ('cylinders', models.CharField(max_length=20)),
                ('valvespercyclinder', models.CharField(max_length=20)),
                ('valvemechanism', models.CharField(max_length=20)),
                ('cyclinder_configuration', models.CharField(max_length=20)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engines', to='vehicle.Variant')),
            ],
            options={
                'verbose_name_plural': 'Engines',
                'verbose_name': 'Engine',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('archived', 'Archived')], default='active', max_length=10)),
                ('showroom_price', models.CharField(max_length=20)),
                ('onroad_price', models.CharField(max_length=20)),
                ('emi', models.CharField(blank=True, max_length=20, null=True)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='vehicle.Variant')),
            ],
            options={
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
    ]
