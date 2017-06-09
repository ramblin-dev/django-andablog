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
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    content = MarkupField()
    is_published = models.BooleanField(default=False)
    published_timestamp = models.DateTimeField(blank=True, null=True, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, editable=True)
    tags = TaggableManager(blank=True)
    preview_content = MarkupField(blank=True)
    preview_image = models.ImageField(blank=True, upload_to='andablog/images')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "entries"

    def get_absolute_url(self):
        return reverse('andablog:entrydetail', args=[self.slug])

    def _insert_timestamp(self, slug, max_length=255):
        """Appends a timestamp integer to the given slug, yet ensuring the
        result is less than the specified max_length.
        """
        timestamp = str(int(time.time()))
        ts_len = len(timestamp) + 1
        while len(slug) + ts_len > max_length:
            slug = '-'.join(slug.split('-')[:-1])
        slug = '-'.join([slug, timestamp])
        return slug

    def _slugify_title(self):
        """Slugify the Entry title, but ensure it's less than the maximum
        number of characters. This method also ensures that a slug is unique by
        appending a timestamp to any duplicate slugs.
        """
        # Restrict slugs to their maximum number of chars, but don't split mid-word
        self.slug = slugify(self.title)
        while len(self.slug) > 255:
            self.slug = '-'.join(self.slug.split('-')[:-1])

        # Is the same slug as another entry?
        if Entry.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            # Append time to differentiate.
            self.slug = self._insert_timestamp(self.slug)

    def save(self, *args, **kwargs):
        self._slugify_title()

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
        return u"{entry} - {image}".format(
            entry=truncatechars(self.entry, 10),
            image=truncatechars(self.image.name, 10),
        )
