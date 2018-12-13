#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 测试发现
"""

import pytest,time,allure,sys
reload(sys)
sys.setdefaultencoding("utf-8")
from android.module.home import Home
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()
from config import *

@allure.feature("测试发现")
@pytest.mark.usefixtures('driver_setup')
class TestFind():

    @pytest.fixture()
    def init(self, scope="class"):
        self.home = Home(self.driver)
        self.home.find_tab()
        logger.info("初始化首页模块")
        yield self.home
        logger.info("结束首页模块")

    @allure.story('测试发现')
    def test_find(self, init):
        logger.info("测试发现")

    @allure.story('测试发现')
    def test_find(self, init):
        logger.info("测试发现")

