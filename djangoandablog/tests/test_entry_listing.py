#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.test import TestCase

from djangoandablog import models


class TestEntryListing(TestCase):

    fixtures = ['three_published_entries']

    def setUp(self):
        self.url = reverse('andablog:entrylist')

    def test_anonymous_get(self):
        """Entries should be listed by descending published timestamp"""
        response = self.client.get(self.url)

        expected_slugs = ['last-post', 'busy-busy', 'welcome']
        actual_slugs = [entry.slug for entry in response.context['entries']]

        self.assertEquals(response.status_code, 200)
        self.assertEquals(actual_slugs, expected_slugs)
        self.assertNumQueries(1)
