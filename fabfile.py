import os

from fabric.api import local
from fabric.context_managers import hide
from fabric.state import output


ROOT = os.path.dirname(os.path.abspath(__file__))
VIRTUALENV = os.path.join(ROOT, 'venv')
PYTHON = os.path.join(VIRTUALENV, 'bin/python')
RUNTESTS_PY = os.path.join(ROOT, 'runtests.py')
PIP = os.path.join(VIRTUALENV, 'bin/pip')
LOCAL_REQUIREMENTS = os.path.join(ROOT, 'local_requirements.txt')
DEMO_MANAGE_PY = os.path.join(ROOT, 'demo/manage.py')


def pip(str_args):
    """Runs the project's pip with the specified shell arguments"""
    local('{} {}'.format(PIP, str_args))


def python(str_args):
    """Runs the project's python with the specified shell arguments"""
    local(' '.join([PYTHON, str_args]))


def clean():
    """Wipes any compiled python files from the project"""
    local('find {} -name "*.pyc" -delete'.format(ROOT))
    local('find {} -name "*.pyo" -delete'.format(ROOT))
    local('find {} -name "*~" -delete'.format(ROOT))
    local('find {} -name "__pycache__" -delete'.format(ROOT))


def reset_demo_db():
    """Resets the demo db."""
    python("{} reset_db --noinput".format(DEMO_MANAGE_PY))


def delete_venv():
    """Deletes the virtualenv"""
    local("rm -rf {}".format(VIRTUALENV))


def create_venv():
    """Creates a virtualenv if it doesn't exist. Installs dependencies"""
    if not os.path.isdir(VIRTUALENV):
        local('virtualenv --distribute {}'.format(VIRTUALENV))
    pip('install --upgrade -r {}'.format(LOCAL_REQUIREMENTS))


def recreate_venv():
    """Deletes and re creates the virtualenv, reinstalling any dependencies"""
    delete_venv()
    create_venv()


def manage(args):
    """Runs the demo's manage.py command with some args"""
    python(' '.join([DEMO_MANAGE_PY, args]))


def test():
    """Runs all tests"""
    manage('test blog djangoandablog')


def runserver():
    """Runs the demo development server"""
    python('{} runserver'.format(DEMO_MANAGE_PY))


def dumpdata(app_target):
    """Dumps data from an app to a named fixture"""
    output['status'] = False
    with hide('running', 'status'):
        manage_args = 'dumpdata --indent=4 {}'.format(app_target)
        manage(manage_args)
