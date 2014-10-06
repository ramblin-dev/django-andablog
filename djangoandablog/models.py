# -*- coding: utf-8 -*-
import time

from django.db import models
from django.utils.text import slugify
from model_utils.models import TimeStampedModel


class Entry(TimeStampedModel):
    """
    Represents a blog Entry.
    Uses TimeStampModel to provide created and modified fields
    """
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, editable=False)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    published_timestamp = models.DateTimeField(blank=True, null=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # Is the same slug as another entry?
        if Entry.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            # Append time to differentiate
            self.slug = "{}-{}".format(self.slug, int(time.time()))
        super(Entry, self).save()
