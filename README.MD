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



## 学习笔记
https://docs.pytest.org/en/latest/example/simple.html

浅谈自动化测试工具 python-uiautomator2
https://testerhome.com/topics/11357