#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import functools
from fabric.api import env, abort, warn, puts
try:
    from configparser import ConfigParser
except:
    from ConfigParser import ConfigParser

BOOL_TRUE = ['True', 'TRUE', 'true', True]
BOOL_FALSE = ['False', 'FALSE', 'false', False]

class EnvConfig(object):
    def __init__(self):
        self.config_parser = ConfigParser()
        self.load_config('core/default_config.ini')

    def load_config(self, file):
        self.config_parser.read(file)
        for section in self.config_parser.sections():
            for option in self.config_parser.options(section):
                val = self.config_parser.get(section, option)
                if re.match(r'^\[.*\]$', val):
                    val = eval(val)
                elif val.isdigit():
                    val = int(val)
                elif val in BOOL_TRUE:
                    val = True
                elif val in BOOL_FALSE:
                    val = False
                env[option] = val

    def pre_init(self):
        #  the Python path to a Django settings module.
        if env.stage == 'product':
            env.django_project_settings = 'settings'
            env.db_init_shell = 'db_init.sh'
        elif env.stage == 'staging':
            env.django_project_settings = 'settings_staging'
            env.db_init_shell = 'db_stage_init.sh'
        else:  # local
            env.django_project_settings = 'settings_staging'
            env.db_init_shell = 'db_stage_init.sh'

        #  hosts to deploy your project, users must be sudoers
        env.hosts = ["%s@%s" % (env.login_user, ip) for ip in env.target_ips]
        pass

def load_config(path):
    if not env.get('load_config'):
        if is_config_file(path):
            env_config = EnvConfig()
            env_config.load_config(path)
            env_config.pre_init()
            env['load_config'] = True
            log("load config '%s' successful!" % path)
        else:
            abort("Please specify the configuration file.")
    else:
        log("The configuration has been loaded in the task("+env.command+")")

def is_config_file(path):
    return os.path.exists(path) and os.path.splitext(path)[1] == '.ini'

def log(msg):
    puts(">>>:::"+str(msg))

def line_between(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        puts('==========BEGIN TASK %s()==========' % func.__name__)
        val = func(*args, **kw)
        puts('==========END   TASK %s()==========' % func.__name__)
        return val
    return wrapper