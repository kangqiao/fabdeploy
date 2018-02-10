#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from fabric.api import env
try:
    from configparser import ConfigParser
except:
    from ConfigParser import ConfigParser

BOOL_TRUE = ['True', 'TRUE', 'true', '1', 1, True]
BOOL_FALSE = ['False', 'FALSE', 'false', '0', 0, False]

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

def log(msg):
    print(">>>"+msg)