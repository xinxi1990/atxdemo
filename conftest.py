#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 创建driver
"""
import os,sys,subprocess,pytest,time
from module.base import Base
import uiautomator2 as ut2
import uiautomator2.ext.htmlreport as htmlreport
from driver import Driver
from config import *
sys.path.append('..')
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


@pytest.fixture()
def driver_setup(request):
    logger.info("app测试开始!")
    request.instance.driver = Driver().init_driver(device_name)
    logger.info("driver初始化")
    request.instance.driver.app_start(pck_name, lanuch_activity, stop=True)
    time.sleep(3)

    def driver_teardown():
        logger.info("app测试结束!")
    request.addfinalizer(driver_teardown)

