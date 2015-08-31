# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20150507_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_name',
            field=models.CharField(verbose_name='profile name', max_length=20, unique=True),
        ),
    ]
