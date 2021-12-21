#! usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2021-12-21
# Author: Liwi


import os
from unittest import TestCase
from everyday_wechat.utils import config

here_dir = os.path.dirname(__file__)

class BaseTestCase(TestCase):
    def setUp(self):
        # config.init()
        pass
