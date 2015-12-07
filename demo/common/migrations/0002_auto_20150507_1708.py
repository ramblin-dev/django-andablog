# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django import VERSION as DJANGO_VERSION


def get_operations():
    """
    This will break things if you upgrade Django to 1.8 having already applied this migration in 1.7.
    Since this is for a demo site it doesn't really matter (simply blow away the DB if you want to go to 1.8)

    Our demo site is a unusual in that we want to run it's tests (for integration testing) in multiple Django versions.
    Typical sites don't have to worry about that sort of thing.
    """
    compatible = (1, 8) <= DJANGO_VERSION < (1, 10)
    if not compatible:
        return []

    return [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login', blank=True),
        ),
    ]


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = get_operations()