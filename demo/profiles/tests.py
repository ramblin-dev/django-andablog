from django.test import TestCase

from . import models
from . import sitemaps
from django.utils import timezone


class TestProfilePage(TestCase):

    fixtures = ['one_user', 'one_profile']

    def setUp(self):
        self.profile = models.UserProfile.objects.get(user__slug=u'superman')
        self.url = self.profile.get_absolute_url()

    def test_anonymous_get(self):
        """Should be able to view a user's profile page"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['profile'], self.profile)
        self.assertNumQueries(1)


class TestUserProfileSitemap(TestCase):

    fixtures = ['three_users', 'three_profiles']

    def setUp(self):
        self.userprofile_map = sitemaps.UserProfileSitemap()
        self.wonder_woman = models.UserProfile.objects.get(user__slug='wonder-woman')

    def test_items(self):
        """All active user profiles should be listed, sorted by most recently joined"""
        # It's a trap!
        self.wonder_woman.user.is_active = False
        self.wonder_woman.user.save()

        actual_profiles = self.userprofile_map.items()

        expected_slugs = ['agent-0014', 'superman']
        actual_slugs = [profile.user.slug for profile in actual_profiles]

        self.assertEqual(actual_slugs, expected_slugs)
        self.assertNumQueries(1)

    def test_last_modified(self):
        """Should be able to get the last update from a profile"""
        superman = models.UserProfile.objects.get(user__slug='superman')

        actual_update = self.userprofile_map.lastmod(self.wonder_woman)

        now = timezone.now()
        self.assertGreaterEqual(now, actual_update)
        self.assertGreaterEqual(actual_update, superman.modified)
