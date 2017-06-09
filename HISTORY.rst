.. :changelog:

History
-------

2.4.0 (2017-06-09)
------------------
New feature: Optional preview_content (markdown) and preview_image fields for direct control of appearance of item in listing.

2.3.0 (2017-06-09)
------------------
Django 1.11 support, drops Django 1.9 support

2.2.0 (2016-09-17)
------------------
Django 1.10 support, drops Django 1.8 support

2.1.1 (2016-01-17)
------------------
Fixes an issue with saving entries in Django 1.9 caused by a previously faulty version of django-markitup.

2.1.0 (2015-12-07)
------------------
Django 1.9 support, drops Django 1.7 support

2.0.0 (2015-10-18)
------------------
Adds support for titles and slugs up to 255 characters in length. **Major: Migration will auto-truncate existing titles that are > 255 characters**
 * Thanks Federico (fedejaure) for the fork that inspired the change.
 * Thanks Brad Montgomery for design input, fix and feature change.

1.4.2 (2015-09-17)
------------------
Fixed unicode support for models
 * Thanks Samuel Mendes for the report and fix.

1.4.1 (2015-09-11)
------------------
Fixed a missing migration bug
 * Thanks bradmontgomery for the report and fix.
 * CI tests now include a missing migration check.

1.4.0 (2015-05-07)
------------------
Support for Django 1.7.x - Django 1.8.x
 * Adds support for Django 1.8
 * Drops support for Django 1.6 and therefore south_migrations

1.3.0 (2015-03-10)
------------------
Authors are now able to see 'draft' (unpublished) versions of their blog entries.
Upgraded taggit to address an issue that was locking us to an older Django 1.7 version.

1.2.2 (2014-12-04)
------------------
Fixed a bug where the Django 1.7.x migration for recent DB changes was somehow missed.

1.2.1 (2014-12-02)
------------------
The author is now selectable when editing entries in the admin.
 * The list is limited to superusers and anyone with an andablog Entry permission.
 * The initial value is the current user.

1.1.1 (2014-12-02)
------------------
Fixed a bug where the tags field was required in the admin.

1.1.0 (2014-12-01)
------------------
Blog entries can now have tags
 * The entry model now supports tags by way of the django-taggit package.
 * This affects the model only, there are no template examples or tags.

1.0.0 (2014-11-20)
------------------
**Backwards Incompatible with 0.1.0.**
This release includes a rename of the django app package from djangoandablog to andablog to better follow
community conventions. This of course is a very large breaking change, which is why the version is 1.0.
As this is the second version and we have been out such a short time. My hope is that few if any people
are using this app yet. If you are, please submit an issue on GitHub and I will try to help you migrate away.

0.1.0 (2014-11-16)
------------------

* First release on PyPI.
