# -*- coding: utf-8 -*-
"""
Project: Wechat-Github
Creator: Liwi
Create time: 2021-12-21 16:38
Introduction:
"""
from unittest import TestCase
import importlib
import path
import os

from everyday_wechat.control.onewords.wufazhuce import get_wufazhuce_info


class BaseTestCase(TestCase):
    def test_get_wufazhuce_(self):
        ok = get_wufazhuce_info()
        print(ok)

    def test_bot_name(self):
        _path = os.path.dirname(__file__)
        print(_path)
        source = 'ownthink_robot'

        addon = importlib.import_module('everyday_wechat.control.bot.' + source, __package__)
        name = addon.BOT_NAME
        print(name)

        loth = importlib.util.find_spec('everyday_wechat.control.bot')
        print(loth)
