# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
from django.db import migrations, models


# The new, maximum length of titles.
TITLE_LENGTH = 255


def truncate_entry_titles(apps, schema_editor):
    """This function will truncate the values of Entry.title so they are
    255 characters or less.
    """
    Entry = apps.get_model("andablog", "Entry")

    for entry in Entry.objects.all():
        # Truncate to 255 characters (or less) but keep whole words intact.
        while len(entry.title) > TITLE_LENGTH:
            entry.title = ' '.join(entry.title.split()[:-1])
        entry.save()


class Migration(migrations.Migration):

    dependencies = [
        ('andablog', '0003_auto_20150826_2353'),
    ]

    operations = [
        migrations.RunPython(truncate_entry_titles)
    ]
