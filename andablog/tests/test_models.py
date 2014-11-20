#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils.text import slugify
from django.utils import timezone

from andablog import models


class TestEntryModel(TestCase):
    """
    Author Note: We don't do much, if any testing, surrounding the Entry author attribute.
    As all of the integration code for them is in the templates.

    TODO: For 1.7, And-a-Blog should provide a Django system check that ensures that get_short_name and
    get_absolute_url have been implemented on the user model as that is what the templates rely on.
    """

    def setUp(self):
        self.entry = models.Entry.objects.create(title=u'First post!', content=u'The best post on the internet.')

    def test_slug_creation(self):
        """The slug field should automatically get set from the title during post creation"""
        self.assertEqual(self.entry.slug, slugify(self.entry.title))

    def test_new_duplicate(self):
        """The slug value should automatically be made unique if the slug is taken"""
        duplicate_entry = models.Entry.objects.create(title=self.entry.title, content=self.entry.content)

        self.assertNotEqual(self.entry.slug, duplicate_entry.slug)
        self.assertIn(self.entry.slug, duplicate_entry.slug)

    def test_title_rename_to_duplicate(self):
        """Upon title rename, the slug value should automatically be made unique if the slug is taken"""
        new_entry_2 = models.Entry.objects.create(title=u'Second post!', content=u'Second best post on the internet.')

        # Rename
        new_entry_2.title = self.entry.title
        new_entry_2.save()

        self.assertNotEqual(self.entry.slug, new_entry_2.slug)
        self.assertIn(self.entry.slug, new_entry_2.slug)

    def test_publishing(self):
        """Test publishing an entry"""
        self.assertFalse(self.entry.is_published)
        self.assertFalse(self.entry.published_timestamp)

        moment_ago = timezone.now()

        self.entry.is_published = True
        self.entry.save()

        self.assertGreaterEqual(self.entry.published_timestamp, moment_ago)

    def test_unpublishing(self):
        """Should be able to pull an entry after it has been published"""
        self.entry.is_published = True
        self.entry.save()

        self.entry.is_published = False
        self.entry.save()

        self.assertFalse(self.entry.is_published)
        self.assertIsNone(self.entry.published_timestamp)
