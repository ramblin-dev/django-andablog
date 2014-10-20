from django.conf.urls import patterns, include, url

from django import VERSION as DJANGO_VERSION

from django.contrib import admin
admin.autodiscover()

home_url = url(r'^$', 'direct_to_template', {'template': 'home.html'})
if DJANGO_VERSION >= (1, 7):
    from django.views.generic import TemplateView
    home_url = url(r'^$', TemplateView.as_view(template_name='home.html'))

urlpatterns = patterns('',
    home_url,
    url(r'^blog/', include('blog.urls')),
    url(r'^profile/', include('profiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
