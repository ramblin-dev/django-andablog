#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase

from andablog import models


class TestEntryDetail(TestCase):

    def setUp(self):
        self.entry_1 = models.Entry.objects.create(title=u'Welcome!', is_published=True)

        self.url = self.entry_1.get_absolute_url()

    def test_published(self):
        """A published entry should be shown"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.entry_1, response.context['entry'])
        self.assertNumQueries(1)

    def test_unpublished(self):
        """An unpublished entry should not be found"""
        self.entry_1.is_published = False
        self.entry_1.save()

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 404)
