from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.template.defaultfilters import truncatewords_html

from .models import Entry


class LatestEntriesFeed(Feed):
    """
    This is just a base class for a blog entry field.
    It should be sub-classed and further refined before use.
    """
    MAX_ENTRIES = 10

    title = 'Latest blog entries'
    description = 'Latest blog entries sorted by newest to oldest.'

    def item_pubdate(self, item):
        return item.published_timestamp

    def item_author_name(self, item):
        if item.author is None:
            return None
        return item.author.get_short_name()

    def item_author_email(self, item):
        if item.author is None:
            return None
        return item.author.email

    def item_author_link(self, item):
        if item.author is None:
            return None
        return item.author.get_absolute_url()

    def link(self):
        return reverse('andablog:entrylist')

    def item_description(self, item):
        # TODO: "Better support for truncating markup" #2
        return truncatewords_html(item.content, 26)

    def item_title(self, item):
        return item.title

    def items(self):
        return Entry.objects.filter(is_published=True).order_by('-published_timestamp')[:self.MAX_ENTRIES]
