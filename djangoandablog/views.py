from django.views.generic import ListView, DetailView

from . import models


class EntriesList(ListView):

    model = models.Entry
    template_name = 'djangoandablog/entry_list.html'
    context_object_name = 'entries'
    paginate_by = 10
    paginate_orphans = 5

    def get_queryset(self):
        queryset = super(EntriesList, self).get_queryset().filter(is_published=True)
        return queryset.order_by('-published_timestamp')


class EntryDetail(DetailView):

    model = models.Entry
    template_name = 'djangoandablog/entry_detail.html'
    context_object_name = 'entry'
    slug_field = 'slug'

    def get_queryset(self):
        return super(EntryDetail, self).get_queryset().filter(is_published=True)
