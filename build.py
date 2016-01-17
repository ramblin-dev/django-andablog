#!/usr/bin/python
import os

import pyntofdjango
MODULE_PATH = os.path.abspath(__file__)
pyntofdjango.setup_pod(MODULE_PATH)

from pynt import task
from pyntofdjango.tasks import python, pip, clean, delete_venv, create_venv, recreate_venv, manage, test_tox, \
    runserver, dumpdata, migrate, docs, venv_bin
from pyntofdjango import utils, project, paths
from pyntcontrib import safe_cd


@task()
def test_venv():
    """Runs all tests on venv"""
    with safe_cd('demo'):
        project.execute_manage('test', 'andablog')
        project.execute_manage('test')

@task()
def loadalldatas():
    """Loads all demo fixtures."""
    dependency_order = ['common', 'profiles', 'blog', 'democomments']
    for app in dependency_order:
        project.recursive_load(os.path.join(paths.project_paths.manage_root, app))


@task()
def reset_db():
    """Recreates the development db"""
    project.execute_manage('reset_db', '--noinput')


@task()
def rebuild_db():
    """Wipes, migrates and loads fixtures"""
    reset_db()
    migrate()
    loadalldatas()


@task()
def rundocserver():
    """Runs the sphinx-autobuild server"""
    with safe_cd('docs'):
        project.venv_execute('sphinx-autobuild', '.', '_build/html')
