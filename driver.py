#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 创建uiautomator2
"""
import atx,time
import subprocess
import uiautomator2  as ut2
from config import *
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()

class Driver():

    def init_driver(self,device_name):
        '''
        初始化driver
        is_clear:清除数据
        :return:
        '''
        try:
            logger.info(device_name)
            d = ut2.connect(device_name)
            # d = ut2.connect("192.168.129.93")
            #logger.info("设备信息:{}".format(d.info))
            # 设置全局寻找元素超时时间
            d.wait_timeout = wait_timeout  # default 20.0
            # 设置点击元素延迟时间
            d.click_post_delay = click_post_delay
            #d.service("uiautomator").stop()
            # 停止uiautomator 可能和atx agent冲突
            logger.info("连接设备:{}".format(device_name))
            return d
        except Exception as e:
            logger.info("初始化driver异常!{}".format(e))



    def init_ios_driver(self, device_name):
        try:
            d = atx.connect("http://localhost:8100")
            d.start_app(bundle_id)
            time.sleep(5)
            return d
        except Exception as e:
            logger.info("初始化ios端driver异常!{}".format(e))



