# -*- coding: utf-8 -*-
import time

from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings

from markitup.fields import MarkupField
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager


class Entry(TimeStampedModel):
    """
    Represents a blog Entry.
    Uses TimeStampModel to provide created and modified fields
    """
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, editable=False)
    content = MarkupField()
    is_published = models.BooleanField(default=False)
    published_timestamp = models.DateTimeField(blank=True, null=True, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, editable=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "entries"

    def get_absolute_url(self):
        return reverse('andablog:entrydetail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # Is the same slug as another entry?
        if Entry.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            # Append time to differentiate
            self.slug = "{}-{}".format(self.slug, int(time.time()))

        # Time to publish?
        if not self.published_timestamp and self.is_published:
            self.published_timestamp = timezone.now()
        elif not self.is_published:
            self.published_timestamp = None

        super(Entry, self).save(*args, **kwargs)


class EntryImage(TimeStampedModel):
    entry = models.ForeignKey(Entry)
    image = models.ImageField(blank=True, upload_to='andablog/images')

    @property
    def image_url(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        return self.image.url

    def __unicode__(self):
        return "{entry} - {image}".format(
            entry=truncatechars(self.entry, 10),
            image=truncatechars(self.image.name, 10),
        )
