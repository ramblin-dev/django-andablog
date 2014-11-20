from django.test import SimpleTestCase
from django.utils.safestring import SafeString

from .. templatetags import andablog_tags


class TestAuthorDisplay(SimpleTestCase):

    def setUp(self):
        class MockAuthor(object):
            def get_short_name(self):
                return 'ShyGuy'
        self.author = MockAuthor()

    def test_none_link(self):
        """Test that our template tag returns just the short name when we get None for the URL"""
        def mock_get_url():
            return None
        self.author.get_absolute_url = mock_get_url

        display = andablog_tags.author_display(self.author)
        self.assertEqual(display, 'ShyGuy')

    def test_empty_link(self):
        """Test that our template tag returns just the short name when we get "" for the URL"""
        def mock_get_url():
            return ""
        self.author.get_absolute_url = mock_get_url

        display = andablog_tags.author_display(self.author)
        self.assertEqual(display, 'ShyGuy')

    def test_no_link_function(self):
        """Test that our template tag returns just the short name when we can not get the URL"""
        display = andablog_tags.author_display(self.author)
        self.assertEqual(display, 'ShyGuy')

    def test_profile_display(self):
        """Test that our template tag returns the short name hyperlinked to the URL"""
        def mock_get_url():
            return 'http://example.com/profile/shyguy'
        self.author.get_absolute_url = mock_get_url

        display = andablog_tags.author_display(self.author)
        self.assertEqual(display, SafeString('<a href="http://example.com/profile/shyguy">ShyGuy</a>'))

    def test_no_short_name(self):
        """Test that our template tag uses the unicode representation when there is no short name"""
        class MockAuthor(object):
            pass
        self.author = MockAuthor()

        display = andablog_tags.author_display(self.author)
        self.assertIn('MockAuthor object', display)
