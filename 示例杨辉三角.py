#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2019/1/3'
# 我不懂什么叫年少轻狂，只知道胜者为王
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""


# def yhTriangle(n):
#     l, index = [1], 0
#     while index < n:
#         yield l
#         l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [l]
#         index += 1
#
#
# for x in yhTriangle(10):
#     print(x)


def createL(l):
    L = [1]
    for x in range(1, len(l)):
        L.append(l[x] + l[x - 1])
    L.append(1)
    return L


def printL(L, W):
    s = ""
    for x in L:
        s += str(x) + "  "
    print(s.center(W))


L = [1]
row = int(input("输入行数："))
width = row * 4  # 设置打印宽度

for x in range(row):
    printL(L, width)
    L = createL(L)
