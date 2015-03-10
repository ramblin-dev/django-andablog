"""
Since we rely on an underlying blog engine we are primarily
testing the integration points of the chosen blog engine. E.g.
 * Are the URLs from the blog engine hooked up correctly?
 * Are we including the blog data into the sitemap?
 * Are we exposing a blog feed?
"""
from django.core.urlresolvers import reverse
from django.test import TestCase

from andablog import models as blogmodels

from .feeds import LatestBlogEntries


class EntryListingTests(TestCase):
    """Posts or not, we just want to make sure we are hooking this up properly"""

    def setUp(self):
        self.url = reverse('andablog:entrylist')

    def test_rendering(self):
        """The listing should render properly"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)


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

        self.assertEqual(expected, actual)

    def test_url(self):
        """Should be able to get the feed items by URL"""
        url = reverse('blog-entry-feed')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestAuthorEntryListing(TestCase):
    """An author looking at the entry listing"""

    fixtures = ['three_users', 'three_profiles', 'three_published_entries']

    def setUp(self):
        an_entry = blogmodels.Entry.objects.get(slug='last-post')
        an_entry.published_timestamp = None
        an_entry.is_published = False
        an_entry.save()

        self.client.login(username='agent0014@example.com', password='secret')

        self.url = reverse('andablog:entrylist')

    def test_draft_listed(self):
        """Our author should see the draft entry."""
        response = self.client.get(self.url)

        expected_slugs = ['last-post', 'busy-busy', 'welcome']
        actual_slugs = [entry.slug for entry in response.context['entries']]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual_slugs, expected_slugs)
        self.assertNumQueries(1)


class TestAuthorEntryDetail(TestCase):
    """An author looking at the entry detail"""

    fixtures = ['three_users', 'three_profiles', 'three_published_entries']

    def setUp(self):
        self.an_entry = blogmodels.Entry.objects.get(slug='last-post')
        self.an_entry.published_timestamp = None
        self.an_entry.is_published = False
        self.an_entry.save()

        self.client.login(username='agent0014@example.com', password='secret')

        self.url = reverse('andablog:entrydetail', args=[self.an_entry.slug])

    def test_draft_detail(self):
        """Our author should be able to view the draft entry."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.an_entry.slug, response.context['entry'].slug)
        self.assertNumQueries(1)