# -*- coding: utf-8 -*-

import sys
import logging

from lib.runner import Runner
from lib.config import Config

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

builder_list = [
    'prepare',
    'app',
    'image',
]

if __name__ == '__main__':
    Runner(builder_list).run(Config.from_env())
