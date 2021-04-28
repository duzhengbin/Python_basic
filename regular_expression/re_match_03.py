# -*- coding: UTF-8 -*-
# 开发作者：火藤
# 开发人员：Meet
# 开发时间：2021/4/28 17:53
# 文件名称：re_match_03.py
# 开发工具：PyCharm
import re

# 要匹配的字符串
string = "Hello 1234567 World_This is a Regex Demo"
# 模式字符串
pattern = r"^Hello\s(\d+)\sWorld"
# 匹配字符串
match = re.match(pattern,string)

if match:
    print(match)                # 获取Match对象
    print(match.group())        # 获取匹配后的字符串
    print(match.group(1))       # 获取匹配后的第1组字符串
    print(match.span())         # 返回匹配字符串的开始与结束
    print(match.end())          # 获取匹配字符串在原始字符串的结束位置
else:
    print("No match!!")  # 匹配不成功
