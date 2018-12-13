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
from android.module.login import Login
from android.module.home import Home


@pytest.mark.usefixtures('driver_setup')
@pytest.mark.run(order=1)
# 指定login先执行
class TestLogin:

    @pytest.fixture()
    def init(self,scope="function"):
        self.home = Home(self.driver)
        self.home.mine_tab()
        self.login = Login(self.driver)
        logger.info("初始化登录模块")
        yield self.login
        logger.info("结束登录模块")


    @allure.story('测试登录')
    @pytest.mark.P0
    def test_login(self,init):
        init.login()
