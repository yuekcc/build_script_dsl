# -*- coding: utf-8 -*-

import unittest

from lib.sh import sha256sum


class TestShellDsl(unittest.TestCase):

    def test_sha256sum(self):
        hash_code = sha256sum('.gitignore')
        self.assertIsNotNone(hash_code)
        print('sha256sum result =', hash_code)
