__author__ = 'Anoop MS'
"""
======
Models
======
Provides base models for other django.model subclass
"""
from django.db import models
from django.db.models import Manager, Model
from django.utils.translation import ugettext as _
from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class ExManager(Manager):
    pass


class ExModel(Model):
    """
    Adds default permissions and some common methods
    .. note:: Always use this class instead of django.db.models.Model
    """
    CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('archived', 'Archived'),
    )
    created_at = AutoCreatedField(_('Updated at'))
    updated_at = AutoLastModifiedField(_('Updated at'))
    status = models.CharField(default='active', choices=CHOICES, max_length=10)

    objects = ExManager()

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        abstract = True
