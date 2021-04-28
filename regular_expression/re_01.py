# -*- coding: UTF-8 -*-
# 开发作者：火藤
# 开发人员：Meet
# 开发时间：2021/4/28 16:26
# 文件名称：re_01.py
# 开发工具：PyCharm

# 匹配字符串是否以”mr_“开头，不区分字母大小写
import re       # 带入re模块
pattern = r"mr\w+"      # 模式字符串
string = "MR_SHOP mr_shop"      # 要匹配的字符串
match = re.match(pattern,string,re.I)       # 匹配字符串，不区分大小写
if match == None:
    print("不成功，未能找到匹配结果")
else:
    print("匹配成功")
    print("匹配值的起始位置：",match.start())
    print("匹配值的结束位置：",match.end())
    print("匹配位置的元组：",match.span())
    print("要匹配的字符串：",match.string)
    print("匹配数据：",match.group())
