# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django import VERSION as DJANGO_VERSION


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    @property
    def operations(self):
        compatible = (1, 8) <= DJANGO_VERSION < (1, 9)
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