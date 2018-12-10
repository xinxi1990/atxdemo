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

# 当设置autouse为True时,
# 在一个session内的所有的test都会自动调用这个fixture
@pytest.fixture(autouse=True)
def driver_setup(request):
    logger.info("app测试开始!")
    request.instance.driver = Driver().init_driver(device_name)
    logger.info("driver初始化")
    request.instance.driver.app_start(pck_name, lanuch_activity, stop=True)
    time.sleep(3)

    def driver_teardown():
        logger.info("app测试结束!")
    request.addfinalizer(driver_teardown)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            print "写入失败截图..."
            f.write(rep.nodeid + extra + "\n")