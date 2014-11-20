============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/WimpyAnalytics/django-andablog/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Andablog could always use more documentation, whether as part of the
official andablog docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/WimpyAnalytics/django-andablog/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to let the code flow from your fingertips? Here's how to set up `django-andablog` for local development.

Get the code
~~~~~~~~~~~~

1. Fork the `django-andablog` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/django-andablog.git

Install Build Tool (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can install and use our make-style tool of choice if you don't want to worry about the virtualenv or navigating the project structure.

    On Linux (one time) from the cloned dir::

        $ sudo pip install pynt

    Or (one time) on windows::

        $ pip install pynt

Install Dependencies
~~~~~~~~~~~~~~~~~~~~

System Packages
^^^^^^^^^^^^^^^
These are necessary for running tox. Which is required if you intend to make changes.

* Python dev package (python-dev on apt)
* Python 3 dev packages (python3-dev on apt)

Python Packages
^^^^^^^^^^^^^^^

Using build script::

    $ pynt create_venv

Or manually:

    1. Create and activate a virtualenv (somewhere)
    2. Change directory to the cloned dir
    3. Install the dev and test dependencies::

        $ pip install -r local_requirements.txt

Making changes
~~~~~~~~~~~~~~

1. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

 Now you can make your changes locally. Make sure to periodically run the tests for the active Python and Django version::

   $ pynt test_venv

 Or run them manually, with the virtualenv activated::

    $ cd demo
    $ python manage.py test
    $ python manage.py test andablog

2. When you're done making changes, check that your changes work with all supported Python and Django versions::

    $ pynt test

 Or manually, with the virtualenv activated::

    $ tox

3. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

4. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Public functions should have docstrings, and add the feature to the list in docs/index.rst.
3. The pull request should work for all supported Python and Django versions, and for PyPy. Check
   https://travis-ci.org/WimpyAnalytics/django-andablog/pull_requests
   and make sure that the tests pass for all configurations.

Tips
----

If you are using our make-style commands you really should never have to activate a virtualenv. Some more common commands.

    Command listing::

        $ pynt -l

    Running the development server::

        $ pynt runserver

    Interacting with demo's manage.py::

        $ pynt manage["help"]

    Load all fixtures in the entire project::

        $ pynt loadalldatas

You are also free to add any new tasks to build.py.
