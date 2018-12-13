#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 测试发布
"""

import pytest,time,allure,json,sys
reload(sys)
sys.setdefaultencoding("utf-8")
from android.module.news import News
from android.module.home import Home
from android.module.push import Push
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()
from config import *

item = json.loads(open('./provide/push.item.json', 'r').read())

@allure.feature("测试发布")
@pytest.mark.usefixtures('driver_setup')
class TestNews:

    @pytest.fixture(params=item)
    def item(self, request):
        return request.param

    @pytest.fixture()
    def init(self,scope="class"):
        self.home = Home(self.driver)
        self.home.push_tab()
        self.push = Push(self.driver)
        logger.info("初始化发布模块")
        yield self.push
        logger.info("结束发布模块")


    @allure.story('测试发布参数化' + '\n' + '使用json文件')
    def test_push_item(self,init,item):
        init.push_item(item['item'])


