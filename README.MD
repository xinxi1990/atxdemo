# 简介
使用uiautomator2+pytest+allure进行Android的UI自动化测试

# 环境搭建

## pytest框架
pip install pytest==3.7

## allure报告
```
命令:
py.test --alluredir=reports
allure generate reports
allure generate reports --clean
allure generate --clean reports -o myreport
用火狐浏览器打开,chrome会404
```


## uiautomator2官方文档
https://github.com/openatx/uiautomator2

## 安装atx-agent
pip uninstall uiautomator2<br>
pip install --pre uiautomator2<br>
python -m uiautomator2 init<br>


## 查看页面元素
pip install weditor<br>
python -m weditor<br>


## 运行命令

测试单个方法: pytest -k test_home_search --alluredir=reports -s <br>
测试单个用例:pytest -s testcase/test_find.py <br>
测试PO级Case: pytest -v -m "P0" --alluredir=reports <br>
不测试PO级Case: pytest -v -m "not P0" --alluredir=reports <br>

## 生成报告
allure generate --clean reports -o myreport

## 无线连接
```
手机的ip地址需要和pc电脑的ip地址在一个网段上
d = ut2.connect("192.168.129.93")
```

## 学习笔记
https://docs.pytest.org/en/latest/example/simple.html


## iOS环境搭建
查看设备中app列表
ideviceinstaller -u 86616cbaa40e52d3f9236ec982dd6f1e933a44bd -l



浅谈自动化测试工具 python-uiautomator2
https://testerhome.com/topics/11357