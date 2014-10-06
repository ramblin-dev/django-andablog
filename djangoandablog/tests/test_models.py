#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils.text import slugify

from djangoandablog import models


class TestEntryModel(TestCase):

    def setUp(self):
        self.entry = models.Entry.objects.create(title=u'First post!', content=u'The best post on the internet.')

    def test_slug_creation(self):
        """The slug field should automatically get set from the title during post creation"""
        self.assertEquals(self.entry.slug, slugify(self.entry.title))

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
