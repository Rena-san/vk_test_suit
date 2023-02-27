import json
import os

from framework.singleton import Singleton

CONFIG_PATH = '/config.json'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class ConfigParser(metaclass=Singleton):
    config = None

    def open_config(self):
        with open(DIR_PATH + CONFIG_PATH, 'r') as fd:
            self.config = json.load(fd)

    def get_config(self):
        if self.config is None:
            self.open_config()
        return self.config
