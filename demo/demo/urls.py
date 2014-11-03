from django.conf import settings
from django.conf.urls import patterns, include, url
from django import VERSION as DJANGO_VERSION
from django.contrib import admin
from django.conf.urls.static import static

from djangoandablog.sitemaps import EntrySitemap

from profiles.sitemaps import UserProfileSitemap

admin.autodiscover()

sitemaps = {
    'profiles': UserProfileSitemap,
    'blog': EntrySitemap,
}

home_url = url(r'^$', 'direct_to_template', {'template': 'home.html'})
if DJANGO_VERSION >= (1, 7):
    from django.views.generic import TemplateView
    home_url = url(r'^$', TemplateView.as_view(template_name='home.html'))

urlpatterns = patterns('',
    home_url,
    url(r'^accounts/', include('allauth.urls')),  # All Auth
    url(r'^blog/', include('blog.urls')),
    url(r'^profile/', include('profiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^markitup/', include('markitup.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Static media hosting in debug mode

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
