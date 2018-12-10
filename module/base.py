#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 对元素基本操作封装
"""

import pytest,time,os,re,yaml,json,sys,xmltodict
import subprocess,base64
sys.path.append("..")
from tools.loggers import JFMlogging
from config import *
logger = JFMlogging().getloger()

class Base():

    def __init__(self, driver):
        self.d = driver
        self.width = self.get_windowsize()[0]
        self.height = self.get_windowsize()[1]

    def click(self, element, logtext):
        '''
        元素点击
        driver: 操作对象
        element:元素名称
        logtext:打印log的文案
        xpath使用方法
        1.包含
        d.xpath(u"//android.widget.TextView[contains(@text,'购买 ¥')]").click()
        2.全匹配
        d.xpath(u"//android.widget.TextView[@text='购买 ¥4.99']").click()
        3.匹配开始字符
        d.xpath(u"//android.widget.TextView[starts-with(@text,'购买 ¥')]").click()
        :return:
        '''
        if str(element).startswith("com"):
            self.d(resourceId=element).click()
        elif re.findall("//", str(element)):
            self.d.xpath(element).click()
        else:
            self.d(text=element).click()
        logger.info("点击元素:{}".format(logtext))



    def send_keys(self,element,sendtext,logtext):
        '''
        文本输入
        driver: 操作对象
        sendtext:输入的文案
        element:元素名称
        logtext:打印log的文案
        :return:
        '''
        self.d(resourceId=element).set_text(sendtext)
        logger.info(logtext)


    def click_web(self,element,logtext):
        '''
        通过文字,点击web页面中的元素
        element=u"文化艺术"
        :return:
        '''

        self.d(description=element).click()
        logger.info("点击元素:{}".format(logtext))


    def double_click(self,x,y,time=0.5):
        '''
        双击
        :return:
        '''
        self.d.double_click(x, y,time)
        logger.info("点击坐标:{},{}".format(x,y))


    def screen_shot(self,pic_name):
        '''
        截图操作
        pic_name:截图名称
        :return:
        '''
        try:
            self.d.screenshot("{}.jpg".format(pic_name))
            logger.info('截图:{}'.format(pic_name))
        except Exception as e:
            logger.info("{}截图失败!{}".format(pic_name,e))


    def get_windowsize(self):
        '''
        获取屏幕尺寸
        :return:
        '''
        window_size = self.d.window_size()
        width = int(window_size[0])
        height = int(window_size[0])
        return width, height

    def swip_up(self, time=0.5):
        '''
        向上滑动
        :return:
        '''
        self.d.drag(self.width / 2, self.height * 3 / 4, self.width / 2, self.height / 4, time)
        logger.info("向上滑动")

    def swip_down(self, time=0.5):
        '''
        向下滑动
        :return:
        '''
        self.d.drag(self.width / 2, self.height / 4, self.width / 2, self.height * 3 / 4, time)
        logger.info("向下滑动")


    def back(self):
        '''
        模拟物理键返回
        :return:
        '''
        self.d.press("back")
        logger.info("点击返回")


    def find_elements(self,element,timeout=5):
        '''
        查找元素是否存在当前页面
        :return:
        '''
        is_exited = False
        try:
            while timeout > 0:
                xml = self.d.dump_hierarchy()
                if re.findall(element,xml):
                    is_exited =  True
                    logger.info("查询到{}".format(element))
                    break
                else:
                    timeout -=1
        except Exception as e:
            logger.info("{}查找失败!{}".format(element,e))
        finally:
            return is_exited




    def assert_exited(self, element):
        '''
        断言当前页面存在要查找的元素,存在则判断成功
        :param driver:
        :return:
        '''
        if self.find_elements(element):
            logger.info("断言{}元素存在,成功!".format(element))
            assert True
        else:
            logger.info("断言{}元素元素存在,失败!".format(element))
            allure.attach(self.screen_shot("截图"), name="截图", attachment_type=AttachmentType.PNG)
            assert False