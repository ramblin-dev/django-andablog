from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^(?P<slug>[A-Za-z0-9-_]+)/$', views.UserProfileDetail.as_view(), name='profile-detail'),
)
