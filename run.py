#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 运行入口
"""

import pytest,os,subprocess
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


def init_env():
    cmd = "python -m uiautomator2 clear-cache"
    subprocess.call(cmd, shell=True)
    cmd = "python -m uiautomator2 init"
    subprocess.call(cmd, shell=True)
    logger.info("初始化运行环境!")

def init_report():
    cmd = "allure generate --clean data -o reports"
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/" + "index.html"
    logger.info("报告地址:{}".format(report_path))


init_env()
pytest.main(["-s","--reruns=2", "android/testcase","--alluredir=data"])
init_report()

