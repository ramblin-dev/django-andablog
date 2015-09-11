# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('andablog', '0002_auto_20141204_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='andablog/images'),
        ),
    ]
