# -*- coding: utf-8 -*-

import logging
from shutil import make_archive

from lib.config import Config
from lib.sh import cd, list_dir, mkdir

logger = logging.getLogger('image')


class Builder:
    def __init__(self, config: Config):
        self._config = config

    def build(self):
        logger.info('start image build')

        cd(self._config.workspace)
        mkdir('uploads')

        pkg_name = f'{self._config.workspace}/uploads/pkg'
        src = f'{self._config.workspace}/dist'
        make_archive(pkg_name, 'gztar', src)
        list_dir(f'{self._config.workspace}/uploads')
        logger.info('done')
