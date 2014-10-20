from django.test import TestCase

from . import models


class TestProfilePage(TestCase):

    fixtures = ['one_user', 'one_profile']

    def setUp(self):
        self.profile = models.UserProfile.objects.get(user__slug=u'superman')
        self.url = self.profile.get_absolute_url()

    def test_anonymous_get(self):
        """Should be able to view a user's profile page"""
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['profile'], self.profile)
        self.assertNumQueries(1)
