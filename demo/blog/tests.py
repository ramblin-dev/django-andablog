"""
Since we rely on an underlying blog engine we are primarily
testing the integration points of the chosen blog engine. E.g.
 * Are the URLs from the blog engine hooked up correctly?
 * Are we including the blog data into the sitemap?
 * Are we exposing a blog feed?
"""
from django.core.urlresolvers import reverse
from django.test import TestCase


class EntryListingTests(TestCase):
    """Posts or not, we just want to make sure we are hooking this up properly"""

    def setUp(self):
        self.url = reverse('andablog:entrylist')

    def test_rendering(self):
        """The listing should render properly"""
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
