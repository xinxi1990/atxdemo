#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

pck_name="com.wuba"
lanuch_activity="com.wuba.activity.launch.LaunchActivity"
device_name="a3f8ca3a"
wait_timeout = 15
click_post_delay = 0.5
lanuch_time = 3
bundle_id = "com.taofang.iphone"
ios_device_name="86616cbaa40e52d3f9236ec982dd6f1e933a44bd"
current_path = os.path.abspath(os.path.dirname(__file__))
screenshot_folder = os.path.join(current_path,"screenshot")
if not os.path.exists(screenshot_folder):
   os.mkdir(screenshot_folder)
   print "创建截图目录:{}".format(screenshot_folder)