from django.views.generic import ListView

import models


class EntriesList(ListView):

    model = models.Entry
    template_name = 'djangoandablog/entry_list.html'
    context_object_name = 'entries'
    paginate_by = 10
    paginate_orphans = 5
