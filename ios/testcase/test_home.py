#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 测试首页
"""
import pytest,time,allure,sys
reload(sys)
sys.setdefaultencoding("utf-8")
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()
from config import *

@allure.feature("测试首页")
@pytest.mark.usefixtures('ios_driver_setup')
class TestHome:

    @pytest.fixture()
    def init(self,scope="class"):
        logger.info("初始化首页模块")
        yield self.home
        logger.info("结束首页模块")

    @allure.story('测试首页搜索')
    def test_home_search(self, init):
        logger.info("测试首页搜索")
