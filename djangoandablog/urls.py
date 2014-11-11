from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.EntriesList.as_view(), name='entrylist'),
    url(r'^(?P<slug>[A-Za-z0-9-_]+)/$', views.EntryDetail.as_view(), name='entrydetail'),
)
