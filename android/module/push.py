#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 测试发布
"""
import pytest,time,allure,sys
reload(sys)
sys.setdefaultencoding("utf-8")
from android.module.base import Base
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()
from config import *

class Push():

    def __init__(self, driver):
        self.base = Base(driver)

    def push_item(self,kewords):
        self.base.click(kewords, kewords)
        self.base.back()