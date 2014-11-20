#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.test import TestCase

from andablog import models


class TestEntryListing(TestCase):

    def setUp(self):
        self.post_1 = models.Entry.objects.create(title=u'Welcome!', is_published=True)
        self.post_2 = models.Entry.objects.create(title=u'Busy Busy', is_published=True)
        self.post_3 = models.Entry.objects.create(title=u'Last Post', is_published=True)
        self.post_4 = models.Entry.objects.create(title=u'Back again!')

        self.url = reverse('andablog:entrylist')

    def test_anonymous_get(self):
        """Only published entries should be listed by descending published timestamp"""
        response = self.client.get(self.url)

        expected_slugs = ['last-post', 'busy-busy', 'welcome']
        actual_slugs = [entry.slug for entry in response.context['entries']]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual_slugs, expected_slugs)
        self.assertNumQueries(1)
