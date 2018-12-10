#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 登录
"""
import allure
from base import Base
from tools.loggers import JFMlogging
from keyconfig import *
from allure_commons.types import AttachmentType
logger = JFMlogging().getloger()

head_image = "com.wuba:id/mycenter_head_image"
username_edit = "com.wuba:id/login_username"
password_edit = "com.wuba:id/login_password"
login_btn = "登录"
head_text = "头像"
username_text = "账号"
password_text = "密码"
my_push = "我的发布"


class Login(Base):

    def __init__(self,driver):
        self.base = Base(driver)

    @allure.story('登录')
    def login(self):
        self.base.click(head_image,head_text)
        self.base.send_keys(username_edit,username,username_text)
        self.base.send_keys(password_edit,password,password_text)
        self.base.click(login_btn, login_btn)
        self.base.assert_exited(my_push)