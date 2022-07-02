# -*- coding: utf-8 -*-

import importlib
import logging

from lib.config import Config

logger = logging.getLogger('runner')


def get_mod_fullname(name):
    return f"builders.{name}"


def _load_builder_classes(builder_list):
    result = []
    for name in builder_list:
        mod_name = get_mod_fullname(name)
        logger.info(f'load builder class, name = {mod_name}')

        try:
            mod = importlib.import_module(mod_name)
            result.append(mod.Builder)
        except:
            logger.error(f'unable to load module: {mod_name}')
            exit(-1)
    return result


class Runner:
    def __init__(self, builder_list):
        self._builder_cls_list = _load_builder_classes(builder_list)

    def run(self, config: Config):
        for builder_cls in self._builder_cls_list:
            builder_cls(config).build()
