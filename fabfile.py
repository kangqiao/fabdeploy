#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import abspath, dirname, join
from fabric.api import env, task
from core.util import EnvConfig, load_config, is_config_file, log, line_between
from core.init import init_machine
from core.setup import setup_project, setup_web_app
from core.deploy import deploy_project, git_pull

@task
@line_between
def config(path=''):
    load_config(path)
    log('load_config:'+str(env['load_config'])+" in the task->'config()'")

@task
@line_between
def init(path=''):
    load_config(path)
    init_machine()

@task
@line_between
def setup(path=''):
    load_config(path)
    setup_project()
    setup_web_app()

@task
@line_between
def deploy(path=''):
    load_config(path)
    deploy_project()

@task
@line_between
def one_step(path=''):
    load_config(path)
    init()
    setup()
    deploy()


