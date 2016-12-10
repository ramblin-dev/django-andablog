====================
Installation & Usage
====================

The easiest way to install Andablog is with pip; this will give you the latest version available on PyPi::

    pip install django-andablog

If you are adventurous (or we are just slow) you can get the latest code directly from the Github repository::

    pip install -e git+https://github.com/WimpyAnalytics/django-andablog.git#egg=django-andablog

The master branch can generally be considered bug free though newer features may be a little half baked.
For more information `see the official Python package installation tutorial <https://packaging.python.org/en/latest/installing.html>`_.

Django Settings
---------------

1. Check Django pre-requisites

 * Confirm that your site's MEDIA_ROOT and MEDIA_URL settings are correct.
 * Django’s site framework should be enabled.
 * The Django admin should be enabled if you wish to use the pre-canned blog administration tools

2. Add to your INSTALLED_APPS::

    INSTALLED_APPS = (
        # ... other applications,
        'andablog',
        'markitup',  # For entry content
        'taggit',  # For entry tags
        'south',   # Only if your site is on Django 1.6
    )

3. Run the migrations::

    $ python manage.py migrate

4. (Optional) Configure andablog to use a markup syntax for blog entries.

    For Markdown, install the Markdown pypi package and add the appropriate `Markitup! settings <https://pypi.python.org/pypi/django-markitup>`_ to your settings.py::

        """ A python-markdown example that allows HTML in the entry content """
        MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': False})
        MARKITUP_SET = 'markitup/sets/markdown/'

    For Textile, add the appropriate `Markitup! settings <https://pypi.python.org/pypi/django-markitup>`_ to your settings.py::

        """ An example using Django's textile package """
        MARKITUP_FILTER = ('django.contrib.markup.templatetags.markup.textile', {})

    To enable a live preview, add the `Markitup! urls <https://pypi.python.org/pypi/django-markitup#installation>`_ to your site's URL hierarchy. Something like this::

        url(r'^markitup/', include('markitup.urls')),


Integrating Andablog into a Site
--------------------------------
The following tasks allow for all possible andablog features. Ignore the items you don't need.

Included Pages
^^^^^^^^^^^^^^
To use the pages provided by andablog add something like this to your site's URL hierarchy::

    (r'^blog/', include('andablog.urls', namespace='andablog')),

Then modify your site's navbar to link to the blog listing. E.g.

    <li><a href="{% url 'andablog:entrylist' %}">Blog</a></li>

Finally, override andablog's base template to inherit from your site's base.html.

    andablog/base.html

.. note:: The andablog templates make no assumptions when it comes to the content of your site's template. All blocks referenced by andablog are prefixed by 'andablog' and you place them how you like.

The demo app has an `example of overriding andablog's base.html <https://github.com/WimpyAnalytics/django-andablog/blob/master/demo/templates/andablog/base.html>`_.

Blog Entry Comments
^^^^^^^^^^^^^^^^^^^

Andablog can use `contrib comments <https://docs.djangoproject.com/en/1.7/ref/contrib/comments/>`_ or any other pluggable commenting system (such as your own).

To provide andablog with comments, override the following template snippets::

    andablog/comments_count_snippet.html
    andablog/comments_snippet.html

Comments using Disqus
++++++++++++++++++++++++++++++++++++++++++++++++++++++

`Disqus <https://disqus.com/>`_ is a service which provides commenting plug-in as a JavaScript and ``<iframe>`` embed for any HTML system. Disqus has free and paid plans.

To use Disqus with Andablog, sign up on Disqus to get your id, add and modify the following ``ndablog/comments_snippet.html`` example::

    <div id="disqus_thread"></div>

    <script type="text/javascript">
        /* * * CONFIGURATION VARIABLES * * */
        var disqus_shortname = 'YOURIDGOESHERE';

        /* * * DON'T EDIT BELOW THIS LINE * * */
        (function() {
            var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
            dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
        })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>

Comments using Django comments framework
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note ::

    Please note that using Django's internal commenting is no longer recommended by Django community.
    Andablog uses it in the demo app to serve as an example of someone having their own custom comments system.

The `comments count snippet <https://github.com/WimpyAnalytics/django-andablog/blob/master/andablog/templates/djangoandablog/comments_count_snippet.html>`_ is used to provide the necessary comment count. The `comments snippet <https://github.com/WimpyAnalytics/django-andablog/blob/master/andablog/templates/andablog/comments_snippet.html>`_ is for listing the comments below the entry.

The demo app has an `example of overriding the snippets <https://github.com/WimpyAnalytics/django-andablog/tree/master/demo/templates/andablog>`_.

Sitemap Support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Andablog provides a andablog.sitemaps.EntrySitemap class that can be used within `The Sitemap Framework <https://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/>`_.

The demo app has an `example using the EntrySitemap <https://github.com/WimpyAnalytics/django-andablog/blob/master/demo/demo/urls.py>`_.

RSS Feed Support
^^^^^^^^^^^^^^^^^^^^^^^^^

Andablog provides a djangoandablog.feeds.LatestEntriesFeed base class that can be sub-classed to provide a blog entries feed class to `The Syndication Feed Framework <https://docs.djangoproject.com/en/dev/ref/contrib/syndication/>`_.

The demo app has an `example feed subclass <https://github.com/WimpyAnalytics/django-andablog/blob/master/demo/blog/feeds.py>`_.

Customizing the Author Display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Any Entry may have an Author, which is a foreignkey to the settings.auth_user_model Model. This auth.User by default or possibly a site's custom user model.

When displaying the author on templates, Andablog uses the andablog_tags.author_display tag to display the author and possibly link to a profile page:

* For Author display: The User model's get_short_name method is called. If not provided, the is used.
* For a hyperlink to an Author page: The User model's get_absolute_url method is called. If this method is absent or returns None/"" the author's display name is not hyperlinked.

.. hint:: If your site implements it's own comment or profile page system you may find the andablog_tags.author_display tag to be useful for the display of other users as well.

The demo app has an `example custom user implementation <https://github.com/WimpyAnalytics/django-andablog/blob/master/demo/common/models.py>`_.

Blog Entry Tags
^^^^^^^^^^^^^^^
The Entry model has a tags field provided by the django-taggit dependency. Out of the box this gives Andablog users
the ability to add tags to an entry and manage them within the admin.

At the moment Andablog does not provide any template examples or tags that display them for you.

There is a (no longer maintained) django-taggit-templatetags project and some (maintained) offshoots to consider. They
weren't up to date enough to package within Andablog.

Package Dependencies
--------------------
* Python 3.4, 3.3 or 2.7
* Django 1.7 or 1.8
* six
* django-model-utils
* django-markitup
* django-taggit
* Pillow

Optional Dependencies
---------------------

* `A Markitup compatible filter package <https://pypi.python.org/pypi/django-markitup#the-markitup-filter-setting>`_ such as Markdown or Textile to have HTML markup in your blog posts

