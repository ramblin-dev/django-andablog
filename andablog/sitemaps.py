from django.contrib.sitemaps import Sitemap

from .models import Entry


class EntrySitemap(Sitemap):
    """
    Sitemap for entries.
    """
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        """
        Return published entries.
        """
        return Entry.objects.filter(is_published=True).order_by('-published_timestamp')

    def lastmod(self, obj):
        """
        Return last modification of an entry.
        """
        return obj.modified
