#!/usr/bin/python
import logging

import os
import contextlib
import sys
from subprocess import check_call, CalledProcessError

from pynt import task

ROOT = os.path.dirname(os.path.abspath(__file__))
DEMO_ROOT = os.path.join(ROOT, 'demo')
VIRTUALENV = os.path.join(ROOT, 'venv')
VENV_PYTHON = os.path.join(VIRTUALENV, 'bin/python')
PIP = os.path.join(VIRTUALENV, 'bin/pip')
LOCAL_REQUIREMENTS = os.path.join(ROOT, 'local_requirements.txt')
DEMO_MANAGE_PY = os.path.join(DEMO_ROOT, 'manage.py')


@contextlib.contextmanager
def _safe_cd(path):
    """
    Usage:
    >>> with _safe_cd(gitrepo_path):
    ... subprocess.call('git status')
    """
    starting_directory = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(starting_directory)


def _execute(command):
    try:
        return check_call(command.split(), shell=False)
    except CalledProcessError as ex:
        print(ex)
        sys.exit(ex.returncode)
    except Exception as ex:
        print('Error: {} with command: {}'.format(ex, command))
        sys.exit(1)


@task()
def pip(str_args):
    """Runs the project's pip with args"""
    _execute('{} {}'.format(PIP, str_args))


@task()
def python(str_args):
    """Runs the project's python with args"""
    _execute(' '.join([VENV_PYTHON, str_args]))


@task()
def clean():
    """Wipes any compiled python files"""
    _execute('find {} -name "*.pyc" -delete'.format(ROOT))
    _execute('find {} -name "*.pyo" -delete'.format(ROOT))
    _execute('find {} -name "*~" -delete'.format(ROOT))
    _execute('find {} -name "__pycache__" -delete'.format(ROOT))


@task()
def delete_venv():
    """Deletes the virtualenv"""
    _execute("rm -rf {}".format(VIRTUALENV))


@task()
def create_venv():
    """Create virtualenv w/local_requirements"""
    if not os.path.isdir(VIRTUALENV):
        _execute('virtualenv --distribute {}'.format(VIRTUALENV))
        _execute('{} -m easy_install pip'.format(VENV_PYTHON))
    pip('install --upgrade -r {}'.format(LOCAL_REQUIREMENTS))


@task()
def recreate_venv():
    """Deletes and re creates virtualenv"""
    delete_venv()
    create_venv()


@task()
def manage(args):
    """Runs the demo's manage.py with args"""
    python(' '.join([DEMO_MANAGE_PY, args]))


@task()
def test():
    """Runs all tests"""
    _execute('tox')


@task()
def runserver():
    """Runs the demo development server"""
    python('{} runserver'.format(DEMO_MANAGE_PY))


@task()
def dumpdata(app_target):
    """Dumps data from an app"""
    # Quiet down pynt...
    logger = logging.getLogger('pynt')
    logger.propagate = False

    manage_args = 'dumpdata --indent=4 {}'.format(app_target)
    manage(manage_args)


@task()
def recursive_load(search_root):
    """Recursively loads all fixtures"""
    for root, dirs, files in os.walk(search_root):
        dir_name = os.path.basename(root)
        if dir_name == 'fixtures':
            fixtures_glob = os.path.join(root, '*.json')
            command = 'loaddata {}'.format(fixtures_glob)
            manage(command)


@task()
def loadalldatas():
    """Loads all demo fixtures."""
    dependency_order = ['common', 'profiles', 'blog', 'democomments']
    for app in dependency_order:
        recursive_load(os.path.join(DEMO_ROOT, app))


@task()
def reset_db():
    """Recreates the development db"""
    manage('reset_db --noinput')
