#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 测试登录
"""
import pytest,time,allure
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()
from config import *
from ios.module.home import Home


@pytest.mark.usefixtures('ios_driver_setup')
@pytest.mark.run(order=1)
# 指定login先执行
class TestLogin:

    @pytest.fixture()
    def init(self,scope="function"):
        self.home = Home(self.driver)
        self.home.mine_tab()
        logger.info("初始化登录模块")
        yield
        logger.info("结束登录模块")

    def test_login(self):
        pass