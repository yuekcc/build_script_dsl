# -*- coding: utf-8 -*-

import logging

from lib.config import Config
from lib.sh import cat, cd, mv, render_file, sha256sum, mkdir

logger = logging.getLogger('app')


class Builder:
    def __init__(self, config: Config):
        self._config = config

    def build(self):
        logger.info('start app build')

        cd(self._config.workspace)
        cat('package.json')
        app_id = sha256sum('package.json')
        app_name = 'a-demo-app'

        logger.info(f'render_file with app_id={app_id}, app_name={app_name}')
        render_file('package.json', {
            r'@{app_name}': 'a-demo-app',
            r'@{app_id}': app_id
        })

        mkdir('dist')
        mv('package.json', 'dist')
        logger.info('done')
