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
from module.login import Login
from module.home import Home


@pytest.mark.usefixtures('driver_setup')
@pytest.mark.run(order=1)
class TestLogin:

    @pytest.fixture()
    def init(self,scope="function"):
        self.home = Home(self.driver)
        self.home.mine_tab()
        self.login = Login(self.driver)
        logger.info("初始化登录")
        yield self.login


    @allure.story('测试登录')
    def test_login(self,init):
        init.login()
