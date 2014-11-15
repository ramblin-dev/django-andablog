=========
Demo Site
=========

No link?
--------

Sorry, we don't yet have the demo hosted somewhere. To try out Andablog you have to pull down the source and run it locally.

Running Locally
---------------

The best way to test out the demo site is to set it up with all fixture data (so there is something to look at).

Using build scripts
~~~~~~~~~~~~~~~~~~~

If you have the `build tools installed <contributing#install-build-tool-optional>`_::

    $ pynt create_venv
    $ pynt rebuild_db
    $ pynt runserver

Manually
~~~~~~~~

1. Create and activate a virtualenv (somewhere)

2. Change directory to the django-andablog cloned dir

3. Install Requirements::

    $ pip install -r local_requirements.txt

4. Recreate the db and setup the database schema::

    $ cd demo
    $ python manage.py reset_db
    $ python manage.py migrate

5. Load all fixtures

    Run this command for every 'fixtures' directory in the project::

        $ python manage.py loaddata someapp/fixtures/*.json

6. Run the server::

    $ python manage.py runserver

Pre-packaged Users
------------------

The demo fixtures include the following users. All users have 'secret' for a password.

Admins
~~~~~~
* admin@example.com

Authors
~~~~~~~
* agent0014@example.com

Regular Users
~~~~~~~~~~~~~
* superman@example.com
* superwoman@example.com
