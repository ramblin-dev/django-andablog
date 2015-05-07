from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.profile_redirect, name='profile-detail-redirect'),
    url(r'^(?P<slug>[A-Za-z0-9-_]+)/$', views.UserProfileDetail.as_view(), name='profile-detail'),
]
