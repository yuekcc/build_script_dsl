# -*- coding: utf-8 -*-

from lib.sh import var


class Config:
    def __init__(self):
        self._workspace = ''

    @property
    def workspace(self):
        return self._workspace

    @classmethod
    def from_env(cls):
        _config = Config()
        _config._workspace = var('WORKSPACE')
        return _config
