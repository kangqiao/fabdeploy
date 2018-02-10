#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os.path import abspath, dirname, join
from fabric.api import env, task

from core.util import EnvConfig, log
from core.init import init_machine
from core.setup import setup_project, setup_web_app
from core.deploy import deploy_project, git_pull

env_config = EnvConfig()
env_config.load_config('config.ini')
env_config.pre_init()

@task
def init():
    init_machine()

@task
def setup():
    setup_project()
    setup_web_app()

@task
def deploy():
    deploy_project()



