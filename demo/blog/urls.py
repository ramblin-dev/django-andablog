from django.conf.urls import include, url
from .feeds import LatestBlogEntries

urlpatterns = [
    url(r'^latest/entries/$', LatestBlogEntries(), name='blog-entry-feed'),
    url(r'^', include('andablog.urls', namespace='andablog')),
]