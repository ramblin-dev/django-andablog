from django.core.urlresolvers import reverse_lazy
from djangoandablog.feeds import LatestEntriesFeed


class LatestBlogEntries(LatestEntriesFeed):
    feed_copyright = 'Example Org'
    title = 'Latest Blog Entries'
    description = 'Updates on the latest blog entries from example.com.'
    link = reverse_lazy('andablog:entrylist')
