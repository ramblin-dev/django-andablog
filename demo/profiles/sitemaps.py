from django.contrib.sitemaps import Sitemap

from . import models


class UserProfileSitemap(Sitemap):

    changefreq = "weekly"
    priority = 0.5
    protocol = 'http'

    def items(self):
        return models.UserProfile.objects.filter(user__is_active=True).order_by('-user__date_joined')

    def lastmod(self, obj):
        return obj.modified
