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
VENV_SPHINX = os.path.join(VIRTUALENV, 'bin/sphinx-build')
VENV_SPHINX_AUTO = os.path.join(VIRTUALENV, 'bin/sphinx-autobuild')
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


def _execute(script, *args):
    popen_args = [script] + list(args)
    try:
        return check_call(popen_args, shell=False)
    except CalledProcessError as ex:
        print(ex)
        sys.exit(ex.returncode)
    except Exception as ex:
        print('Error: {} with script: {} and args {}'.format(ex, script, args))
        sys.exit(1)


def _execute_pip(*args):
    _execute(PIP, *args)


def _execute_python(*args):
    _execute(VENV_PYTHON, *args)


def _execute_manage(*args):
    _execute_python(DEMO_MANAGE_PY, *args)


@task()
def pip(*str_args):
    """Runs the project's pip with args"""
    _execute_pip(*str_args)  # This will be one arg to popen


@task()
def python(*str_args):
    """Runs the project's python with args"""
    _execute_python(*str_args)


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
    _execute('rm', '-rf', VIRTUALENV)


@task()
def create_venv():
    """Create virtualenv w/local_requirements"""
    if not os.path.isdir(VIRTUALENV):
        _execute('virtualenv', '--distribute', VIRTUALENV)
        _execute_python('-m', 'easy_install', 'pip')
    _execute_pip('install', '--upgrade', '-r', LOCAL_REQUIREMENTS)


@task()
def recreate_venv():
    """Deletes and re creates virtualenv"""
    delete_venv()
    create_venv()


@task()
def manage(*arg_string):
    """Runs the demo's manage.py with args"""
    _execute_manage(*arg_string)  # Shows as one arg to manage.py


@task()
def test(flush=False):
    """Runs all tests for all environments."""
    args = ['tox']
    if flush:
        args.append('-r')
    _execute(*args)


@task()
def test_venv():
    """Runs all tests on venv"""
    with _safe_cd('demo'):
        _execute_manage('test', 'andablog')
        _execute_manage('test')


@task()
def runserver():
    """Runs the demo development server"""
    _execute_manage('runserver')


@task()
def dumpdata(app_target):
    """Dumps data from an app"""
    # Quiet down pynt...
    logger = logging.getLogger('pynt')
    logger.propagate = False

    _execute_manage('dumpdata', '--indent=4', app_target)


@task()
def recursive_load(search_root):
    """Recursively loads all fixtures"""
    for root, dirs, files in os.walk(search_root):
        dir_name = os.path.basename(root)
        if dir_name == 'fixtures':
            for file_name in files:
                fixture_path = os.path.join(root, file_name)
                _execute_manage('loaddata', fixture_path)


@task()
def loadalldatas():
    """Loads all demo fixtures."""
    dependency_order = ['common', 'profiles', 'blog', 'democomments']
    for app in dependency_order:
        recursive_load(os.path.join(DEMO_ROOT, app))


@task()
def reset_db():
    """Recreates the development db"""
    _execute_manage('reset_db', '--noinput')


@task()
def migrate():
    """Migrates the development db"""
    _execute_manage('migrate')


@task()
def rebuild_db():
    """Wipes, migrates and loads fixtures"""
    reset_db()
    migrate()
    loadalldatas()


@task()
def docs():
    """Makes the docs"""
    with _safe_cd('docs'):
        _execute(VENV_SPHINX, '-b', 'html', '.', '_build/html')


@task()
def rundocserver():
    """Runs the sphinx-autobuild server"""
    with _safe_cd('docs'):
        _execute(VENV_SPHINX_AUTO, '.', '_build/html')


@task()
def readme_rst():
    """Update README.rst from README.md"""
    _execute_python('readme_rst.py')
