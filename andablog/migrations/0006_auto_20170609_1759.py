# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('andablog', '0005_auto_20151017_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='_preview_content_rendered',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='entry',
            name='preview_content',
            field=markitup.fields.MarkupField(blank=True, no_rendered_field=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='preview_image',
            field=models.ImageField(blank=True, upload_to='andablog/images'),
        ),
    ]
