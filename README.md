django-andablog
===============

A blog app that is intended to be embedded within an existing Django site.

[![Build Status](https://travis-ci.org/WimpyAnalytics/django-andablog.svg?branch=master)](https://travis-ci.org/WimpyAnalytics/django-andablog)

### Using Andablog
* [right out](https://www.youtube.com/watch?feature=player_detailpage&v=xOrgLj9lOwk#t=108)
* Packaged templates utilize a site-provided base template without block name conflicts.
* A URL hierarchy to include at /blog (or wherever)
* Class based generic views that can be used directly
* A Django sitemaps EntrySitemap class
* A base class for an entries feed
* Utilizing a site-provided profile page as the author profile page.
* Python2.7 and 3 support
* Full support for current and 1 previous Django release E.g. For 1.6 and 1.7
 * Custom User Models
 * South migrations
 * Django migrations
* Official (not beta or candidate) Django release tickets are prioritized over new features as to not hold a site's upgrade back.
* A demo application.

### Not Features
These features are [right out](https://www.youtube.com/watch?feature=player_detailpage&v=xOrgLj9lOwk#t=108). If you are looking for one of them, andablog is not for you.
* Providing a pre-packaged User model. You must supply a relation string for andablog to consider the author.
* User/Author Profile pages. These are implemented by the site and linked to by andablog.
* Constructing the author display name or URL. As such the site's user model must implement get_short_name for author display and get_absolute_url for author profile linking.

## Origin Story
At the time of andablog's creation, most Django blog apps (not CMS frameworks) were generally designed to meet one of three use cases.

1. To be used as a standalone site with the app's URL hierarchy starting at '/'.
2. Embedded within an existing site with the app's URL hierarchy starting at a custom location, like '/blog'.
3. Support for both but with a default configuration providing #1 or #2 (usually #1) working out of the box.

django-andablog is intended to address #2 while __fully__ supporting the current Django release and one back.
