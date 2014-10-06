#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.test import TestCase

from djangoandablog import models


class TestEntryListing(TestCase):

    def setUp(self):
        self.url = reverse('andablog:entrylist')

    def test_anonymous_get(self):
        response = self.client.get(self.url)

        expected_ids = [2, 1, 3]
        actual_ids = [entry for entry in response.context['entries']]

        self.assertEquals(response.status_code, 200)
        self.assertEquals(actual_ids, expected_ids)
        self.assertNumQueries(1)
