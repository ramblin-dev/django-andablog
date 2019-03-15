# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from markupfield.fields import MarkupField
import model_utils.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('content', MarkupField(default_markup_type='markdown')),
                ('is_published', models.BooleanField(default=False)),
                ('published_timestamp', models.DateTimeField(null=True, editable=False, blank=True)),
                ('_content_rendered', models.TextField(editable=False, blank=True)),
                ('author', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EntryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('image', models.ImageField(upload_to=b'andablog/images', blank=True)),
                ('entry', models.ForeignKey(to='andablog.Entry', on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
