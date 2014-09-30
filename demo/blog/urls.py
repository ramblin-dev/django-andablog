from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^', include('djangoandablog.urls', namespace='andablog')),
)
