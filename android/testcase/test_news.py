# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 测试消息中心
"""
import pytest,time,allure
from android.module.news import News
from android.module.home import Home
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()
from config import *

@allure.feature("测试消息中心")
@pytest.mark.usefixtures('driver_setup')
class TestNews:

    @pytest.fixture()
    def init(self,scope="class"):
        self.home = Home(self.driver)
        self.home.news_tab()
        self.news = News(self.driver)
        logger.info("初始化消息模块")
        yield self.news
        logger.info("结束消息模块")

    @pytest.mark.flaky(reruns=5, reruns_delay=2)
    @allure.story('测试精选活动')
    def test_news_good(self,init):
        init.news_good()


