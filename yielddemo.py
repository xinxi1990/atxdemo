#!/usr/bin/env python
# -*- coding: utf-8 -*-

def yt():
    print "第一次打印"
    yield 0
    print("第二次打印")

if __name__ == '__main__':
    a = yt()
    print next(a)
    print next(a)
