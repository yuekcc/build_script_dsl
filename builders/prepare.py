# -*- coding: utf-8 -*-

import logging

from lib.config import Config
from lib.sh import mkdir, cd, list_dir

logger = logging.getLogger('prepare')


def make_package_json(output):
    with open(output, 'w') as writer:
        writer.write("""{ "name": "@{app_name}", "version": "1.0.0", "id": "@{app_id}" }""")


class Builder:
    def __init__(self, config: Config) -> None:
        self._config = config

    def build(self):
        mkdir(self._config.workspace)
        cd(self._config.workspace)

        package_json = f'{self._config.workspace}/package.json'
        make_package_json(package_json)

        list_dir()
        logger.info('prepare build')
