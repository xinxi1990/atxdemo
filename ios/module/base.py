#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 对元素基本操作封装
"""

import pytest,time,os,re,yaml,json,sys,xmltodict
import allure
from allure_commons._allure import attach
# from allure.constants import AttachmentType
from allure_commons.types import AttachmentType
import subprocess,base64
sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")
from tools.loggers import JFMlogging
from config import *
logger = JFMlogging().getloger()



class Base():

    def __init__(self, driver):
        self.d = driver
    

