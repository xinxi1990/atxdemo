#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 消息中心
"""
import pytest,os,subprocess
from base import Base
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


good_jobs = "精选活动"

class News(Base):
    def __init__(self, driver):
        self.base = Base(driver)

    def news_good(self):
        self.base.click(good_jobs,good_jobs)
