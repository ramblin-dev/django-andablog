from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.EntriesList.as_view(), name='entrylist'),
)
