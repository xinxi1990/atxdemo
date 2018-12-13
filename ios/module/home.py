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
searcher = ""
search_edit = ""
search_text = "文员"


class Home(Base):

    def __init__(self,driver):
        self.driver = driver

    def home_tab(self):
        self.driver(name=home).click()

    def find_tab(self):
        self.driver(name=find).click()

    def mine_tab(self):
        self.driver(name=mine).click()

    def home_more_search(self,kewords):
        pass

    def home_more(self):
        pass

    def home_guesslike(self):
        pass
