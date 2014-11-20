#!/usr/bin/env python
# -*- coding: utf-8 -*-

import six
from django.core.urlresolvers import reverse
from django.template.defaultfilters import truncatewords
from django.test import TestCase

from andablog import models, feeds


class TestLatestEntriesFeed(TestCase):

    def setUp(self):
        self.post_1 = models.Entry.objects.create(title=u'Welcome!', is_published=True)
        self.post_2 = models.Entry.objects.create(title=u'Busy Busy', is_published=True)
        self.post_3 = models.Entry.objects.create(title=u'Last Post', is_published=True)
        self.post_4 = models.Entry.objects.create(title=u'Back again!')

        self.feed = feeds.LatestEntriesFeed()

    def test_feed_properties(self):
        """The base entry feed should return the last 10 entries by default"""
        actual_entries = self.feed.items()

        expected_slugs = ['last-post', 'busy-busy', 'welcome']
        actual_slugs = [entry.slug for entry in actual_entries]

        self.assertEqual(self.feed.link(), reverse('andablog:entrylist'))
        self.assertEqual(actual_slugs, expected_slugs)
        self.assertNumQueries(1)

    def test_feed_max(self):
        """Should only return ten by default"""
        for x in range(8):
            models.Entry.objects.create(title=u'Ni' + six.text_type(x), is_published=True)

        self.assertEqual(self.feed.items().count(), 10)


class TestLatestEntriesFeedItem(TestCase):

    def setUp(self):
        self.entry = models.Entry.objects.create(title=u'Welcome!', is_published=True)

        self.feed = feeds.LatestEntriesFeed()

    def test_item_properites(self):
        """A base entry feed should implement all item specific properties"""
        expected = (
            self.entry.published_timestamp,
            self.entry.title,
            None,
            None,
            None,
            truncatewords(self.entry.content, 26)
        )
        actual = (
            self.feed.item_pubdate(self.entry),
            self.feed.item_title(self.entry),
            self.feed.item_author_name(self.entry),
            self.feed.item_author_email(self.entry),
            self.feed.item_author_link(self.entry),
            self.feed.item_description(self.entry),
        )

        #NOTE: Populated author properties testing is covered in the demo site tests
        self.assertEqual(expected, actual)
