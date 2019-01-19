#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1.输入苹果的单价
price_str = input("苹果的单价")

# 2. 输入苹果的重量
weight_str = input("苹果的重量")

# 3.计算支付的总金额
#注意：两个字符串之间不能用乘法
# money = price_str * weight_str

#1>将价格转成成小数
price = float(price_str)
#2>将重量转换成小数
weight = float(weight_str)
#3>用两个小数计算苹果的最终金额
money = price * weight

print(money)