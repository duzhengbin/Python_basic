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
print(match)
string = "项目名称MR_SHOP mr_shop"
match = re.match(pattern,string,re.I)       # 匹配字符串，不区分大小写
print(match)        # 输出匹配结果