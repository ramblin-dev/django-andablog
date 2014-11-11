from django.conf.urls import patterns, include, url
from .feeds import LatestBlogEntries

urlpatterns = patterns('',
    url(r'^latest/entries/$', LatestBlogEntries(), name='blog-entry-feed'),
    (r'^', include('djangoandablog.urls', namespace='andablog')),
)
