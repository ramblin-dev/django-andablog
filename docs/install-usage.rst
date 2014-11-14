====================
Installation & Usage
====================

The easiest way to install Andablog is with pip; this will give you the latest version available on PyPi:::

    pip install django-andablog

If you are adventurous (or we are just slow) you can get the latest code directly from the Github repository:::

    pip install -e git+https://github.com/WimpyAnalytics/django-andablog.git#egg=django-andablog

The master branch can generally be considered bug free though newer features may be a little half baked.

Django Settings
---------------

1. Check Django pre-requisites
 * Confirm that the site's MEDIA_ROOT and MEDIA_URL settings are correct.
 * Django’s site framework should be enabled.
 * The Django admin should be enabled if you wish to use the pre-canned blog administration tools

2. Add to your INSTALLED_APPS::

    INSTALLED_APPS = (
        # ... other applications,
        'djangoandablog',
        'markitup',
        'south',   # Only if the site is on Django 1.6
    )

3. (Optional) Configure andablog to use a markup syntax for blog entries.

    For Markdown, install the Markdown pypi package and add the appropriate `Markitup! settings <https://pypi.python.org/pypi/django-markitup>`_ to your settings.py::

        """ A python-markdown example that allows HTML in the entry content """
        MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': False})
        MARKITUP_SET = 'markitup/sets/markdown'

    For Textile, add the appropriate `Markitup! settings <https://pypi.python.org/pypi/django-markitup>`_ to your settings.py::

        """ An example using Django's textile package """
        MARKITUP_FILTER = ('django.contrib.markup.templatetags.markup.textile', {})

    To enable a live preview, add the `Markitup! urls <https://pypi.python.org/pypi/django-markitup#installation>`_ to the site's URL hierarchy. Something like this::

        url(r'^markitup/', include('markitup.urls')),


Integrating andablog into a site
--------------------------------
The following tasks allow for all possible andablog features. Ignore the items you don't need.

Included Pages
^^^^^^^^^^^^^^
To use the pages provided by andablog add something like this to the site's URL hierarchy::

    (r'^blog/', include('djangoandablog.urls', namespace='andablog')),

Then override andablog's base template to inherit from the site's base.html.

    djangoandablog/base.html

.. note:: The andablog templates make no assumptions when it comes to the content of the site's template. All blocks referenced by andablog are prefixed by 'andablog' and it is up to the site's code to place them appropriately.

The demo app has an `example implementation <https://github.com/WimpyAnalytics/django-andablog/blob/master/demo/templates/djangoandablog/base.html>`_.

Blog Entry Comments
^^^^^^^^^^^^^^^^^^^

To provide andablog with comments, override the following template snippets::

    djangoandablog/comments_count_snippet.html
    djangoandablog/comments_snippet.html

The `comments count snippet <https://github.com/WimpyAnalytics/django-andablog/blob/master/djangoandablog/templates/djangoandablog/comments_count_snippet.html>`_ is used to provide the necessary comment count. The `comments snippet <https://github.com/WimpyAnalytics/django-andablog/blob/master/djangoandablog/templates/djangoandablog/comments_snippet.html>`_ is for listing the comments below the entry.

The demo app has an `example implementation <https://github.com/WimpyAnalytics/django-andablog/tree/master/demo/templates/djangoandablog>`_.

Adding blog entries to the sitemap
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Andablog provides a djangoandablog.sitemaps.EntrySitemap class that can be used within `The Sitemap Framework <https://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/>`_.

The demo app has an `example implementation <https://github.com/WimpyAnalytics/django-andablog/blob/master/demo/demo/urls.py>`_.

Providing an entries feed
^^^^^^^^^^^^^^^^^^^^^^^^^

Andablog provides a djangoandablog.feeds.LatestEntriesFeed base class that can be sub-classed to provide a blog entries feed class to `The Syndication Feed Framework <https://docs.djangoproject.com/en/dev/ref/contrib/syndication/>`_.

The demo app has an `example implementation <https://github.com/WimpyAnalytics/django-andablog/blob/master/demo/blog/feeds.py>`_.

Customizing the author display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO

Package Dependencies
--------------------
* Python 3.4, 3.3 or 2.7
* Django 1.6 or 1.7
* six
* django-model-utils
* django-markitup
* Pillow

Optional Dependencies
---------------------

* South, if the site uses Django 1.6
* `A Markitup compatible filter package <https://pypi.python.org/pypi/django-markitup#the-markitup-filter-setting>`_ such as Markdown or Textile

