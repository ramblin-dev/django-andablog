"""
Since we rely on an underlying blog engine we are primarily
testing the integration points of the chosen blog engine. E.g.
 * Are the URLs from the blog engine hooked up correctly?
 * Are we including the blog data into the sitemap?
 * Are we exposing a blog feed?
"""
from django.core.urlresolvers import reverse
from django.test import TestCase

from djangoandablog import models as blogmodels

from feeds import LatestBlogEntries


class EntryListingTests(TestCase):
    """Posts or not, we just want to make sure we are hooking this up properly"""

    def setUp(self):
        self.url = reverse('andablog:entrylist')

    def test_rendering(self):
        """The listing should render properly"""
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)


class LatestEntriesFeed(TestCase):
    """We want to make sure we hooked up the entry feed properly"""

    fixtures = ['three_users', 'three_profiles', 'three_published_entries']

    def setUp(self):
        self.feed = LatestBlogEntries()

    def test_author_details(self):
        """Test that our custom user is integrating properly"""
        an_entry = blogmodels.Entry.objects.get(slug='last-post')

        expected = (
            an_entry.published_timestamp,
            an_entry.author.profile_name,
            an_entry.author.email,
            an_entry.author.get_absolute_url()
        )

        actual = (
            self.feed.item_pubdate(an_entry),
            self.feed.item_author_name(an_entry),
            self.feed.item_author_email(an_entry),
            self.feed.item_author_link(an_entry),
        )

        self.assertEquals(expected, actual)

    def test_url(self):
        """Should be able to get the feed items by URL"""
        url = reverse('blog-entry-feed')

        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
