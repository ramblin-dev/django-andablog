#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils.text import slugify

from . import models


class TestCustomUserModel(TestCase):

    def setUp(self):
        self.user = models.User.objects.create(
            name=u'Clark Jerome Kent',
            profile_name=u'Superman',
            email=u'manofsteel1938@example.com',
        )

    def test_slug_creation(self):
        """The slug field should automatically get set from the profile name during user creation"""
        self.assertEqual(self.user.slug, slugify(self.user.profile_name))

    def test_short_name(self):
        """The short name function should be the profile name"""
        self.assertEqual(self.user.profile_name, self.user.get_short_name())
