# -*- coding: UTF-8 -*-
# 开发作者：火藤
# 开发人员：Meet
# 开发时间：2021/4/28 17:08
# 文件名称：re_match_02.py
# 开发工具：PyCharm
import re

line = "Cats are smarter than dogs"     # 要匹配的字符串
pattern = r"(.*) are (.*?) .*"        # 模式字符串
match = re.match(pattern,line,re.M | re.I)
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串

if match:       # 匹配成功后执行的操作
    print("match.group() : ", match.group())        # 匹配数据
    print("match.group(1) : ", match.group(1))      # 获取匹配的第1组数据
    print("match.group(2) : ", match.group(2))      # 获取匹配的第2组数据
else:
    print("No match!!")     # 匹配不成功