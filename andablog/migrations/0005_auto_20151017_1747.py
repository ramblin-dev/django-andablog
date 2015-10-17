# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andablog', '0004_shorten_entry_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.SlugField(unique=True, editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
