#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils import timezone

from andablog import models, sitemaps


class TestEntrySitemap(TestCase):

    def setUp(self):
        self.post_1 = models.Entry.objects.create(title=u'Welcome!', is_published=True)
        self.post_2 = models.Entry.objects.create(title=u'Busy Busy', is_published=True)
        self.post_3 = models.Entry.objects.create(title=u'Last Post', is_published=True)
        self.post_4 = models.Entry.objects.create(title=u'Back again!')
        self.entry_map = sitemaps.EntrySitemap()

    def test_items(self):
        """Only published entries should be listed by descending published timestamp"""
        actual_entries = self.entry_map.items()

        expected_slugs = ['last-post', 'busy-busy', 'welcome']
        actual_slugs = [entry.slug for entry in actual_entries]

        self.assertEqual(actual_slugs, expected_slugs)
        self.assertNumQueries(1)

    def test_last_modified(self):
        """Should be able to get the last update from an entry"""
        actual_update = self.entry_map.lastmod(self.post_3)

        now = timezone.now()
        self.assertGreaterEqual(now, actual_update)
        self.assertGreaterEqual(actual_update, self.post_1.modified)
