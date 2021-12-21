# -*- coding: utf-8 -*-
"""
Project: Wechat-Github
Creator: Liwi
Create time: 2021-12-21 16:40
Introduction:
"""
from unittest import TestCase

from everyday_wechat.control.rubbish.atoolbox_rubbish import get_atoolbox_rubbish

class BaseTestCase(TestCase):
    def test_atoolbox_rubbish(self):
        key = '牛'
        ok = get_atoolbox_rubbish(key)
        print(ok)
