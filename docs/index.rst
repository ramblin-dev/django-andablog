===============================
Django and a Blog
===============================

A blog app that is only intended to embed within an existing Django site.

* Free software: BSD license `(source) <https://github.com/WimpyAnalytics/django-andablog>`_
* Compatible with Django 1.7 and 1.6
* Compatible with Python 3.4, 3.3 and 2.7

Getting Started
---------------

.. toctree::
   :maxdepth: 2

   install-usage

Features
--------
This list will likely grow slowly. Priorities are Bug Fixes > Django Release Compatibility > Bad Jokes > Features.

* Blog administration through Django admin
* Markdown, Textile or plain text support through django-markitup
* Blog Entry tag management through django-taggit.
* Template block names are prefixed as to not conflict with the those used by the site.
* A URL hierarchy to include at /blog (or wherever)
* A Django sitemaps EntrySitemap class
* A base class for an entries feed
* Utilizing a site-provided profile page as the author profile page
* Easy comment integration. Simply override a template snippet
* Support for custom User Models
* Django migrations
* South migrations (Until we drop Django 1.6)
* Class based generic views that can be used directly
* A demo application.
* Django upgrade friendly: Most recently released major Django version and 1 back

Not Features
------------
.. role:: strike
    :class: strike

These features are `right out <https://www.youtube.com/watch?feature=player_detailpage&v=xOrgLj9lOwk#t=108>`_. If you are looking for one of them, andablog may not be right for you.

* A User model. Andablog uses the settings.auth_user_model relation string for the author.
* Author Profile pages. These can be implemented by the site and linked to by andablog.
* Comments on blog entries. Though help is provided. In the form of a template snippet reference as well as a template tag that can be used for user display/linking.
* Constructing the author display name or URL. A provided User model must implement get_short_name for author display and get_absolute_url for author profile linking.
* Search. Since Andablog is only intended to be packaged with an existing site it would most likely become redundant.
* Support for 3 or more Django major releases. Sorry, if you want to proceed you will have to fork until your site catches up.

Trying out the demo site
------------------------

.. toctree::
   :maxdepth: 2

   demo-site

Contributing to the project
---------------------------

Checkout the `project page <https://github.com/WimpyAnalytics/django-andablog>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

