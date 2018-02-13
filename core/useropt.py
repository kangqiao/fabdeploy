#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import copy
from datetime import datetime
from os.path import basename, abspath, dirname, isfile, join
from fabric.api import env, puts, abort, cd, hide, task
from fabric.operations import sudo, settings, run
from fabric.contrib import console
from fabric.contrib.files import upload_template
from core.init import test_configuration, _verify_sudo
from fabric.colors import _wrap_with, green

from core.util import line_between, load_config
from core.setup import virtenvsudo

@task
@line_between
def create_super_user(path=''):
    load_config(path)
    with cd(env.django_project_root):
        virtenvsudo('python manage.py createsuperuser')
