from __future__ import print_function
import sys
import os
import requests
import logging
import json
from os.path import dirname
from jsonschema import validate
import importlib
import pkgutil


logger = logging.getLogger(__name__)

logging.root.setLevel(logging.INFO)


class Plugin():

    def __init__(self,halo):
        #init vars
        self.halo = halo

        #print(str(halo.settings))
        #halo.cli.log("xxx")

        #init work on halo config
        #if self.halo.config ...

        self.name = 'tester1'
        self.desc = 'test settings file'

        # set commands
        self.commands = {
            'test2': {
                'usage': "test this for your HALO project",
                'lifecycleEvents': ['resources', 'functions'],
                'commands': {
                    'subtest': {
                        'lifecycleEvents': ['resources1', 'functions1'],
                        'usage': "sub test this for your HALO project"
                    }
                }
            },
            'valid2': {
                'usage': "do this for your HALO project",
                'lifecycleEvents': ['resources', 'functions'],
                'options': {
                    'attribute': {
                        'usage': 'Name of the attribute',
                        'required': True,
                        'shortcut': 'a',
                        'default': 'dev'
                    },
                    'value': {
                        'usage': 'Value of the attribute',
                        'shortcut': 'v'
                    }
                },
            },
        }

        # set hooks
        self.hooks = {
            'before:valid2:resources': self.before_valid_resources,
            'valid2:resources': self.valid_resources,
            'after:valid2:functions': self.after_valid_functions,
        }

        #logger.info('finished plugin')

    def run(self,options):
        self.options = options

    def before_valid_resources(self):
        pass

    def valid_resources(self):
        ret = self.halo.valid(self.halo.cli.halo_settings, self.halo.cli.valid_service, self.halo.cli.valid_conn)
        if ret == 0:
            print("finished valid seccessfuly")
        return ret

    def after_valid_functions(self):
        pass

