#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 首页
"""
import pytest
from base import Base
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()

home = "首页"
find = "发现"
push = "发布"
news = "消息"
mine = "我的"
search = "搜索"
more = "更多"
guesslike = "推荐"
searcher = "com.wuba:id/toolbar_searcher"
search_edit = "com.wuba:id/searcherInputEditText"
search_text = "文员"


class Home(Base):

    def __init__(self,driver):
        self.base = Base(driver)

    def home_tab(self):
        self.base.click(home,home)

    def find_tab(self):
        self.base.click(find,find)

    def push_tab(self):
        self.base.click(push, push)

    def news_tab(self):
        self.base.click(news, news)

    def mine_tab(self):
        self.base.click(mine,mine)

    def home_search(self):
        self.base.click(searcher,search)
        self.base.send_keys(search_edit,search_text,search_text)

    def home_more_search(self,kewords):
        self.base.click(searcher, search)
        self.base.send_keys(search_edit, kewords, search_text)
        self.base.back()
        self.base.back()

    def home_more(self):
        self.base.click(more,more)

    def home_guesslike(self):
        self.base.swip_down_element(guesslike)
        self.base.assert_exited(guesslike)
