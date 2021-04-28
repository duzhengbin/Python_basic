# -*- coding: UTF-8 -*-
# 开发作者：火藤
# 开发人员：Meet
# 开发时间：2021/4/28 18:41
# 文件名称：re_match_4.py
# 开发工具：PyCharm
import re

# 要匹配的字符串
string = "Hello 1234567 World_This is a Regex Demo"
# 模式字符串(贪婪匹配）
pattern_1 = r"^He.*(\d+).*Demo$"
# 匹配字符串
match_1 = re.match(pattern_1,string)
# 获取匹配结果
if match_1:
    print(match_1)  # 获取Match对象
    print(match_1.group())  # 获取匹配后的字符串
    print(match_1.group(1))
else:
    print("No match!!")

# 模式字符串（非贪婪匹配）
pattern_2 = r"^He.*?(\d+).*Demo$"
# 匹配字符串
match_2 = re.match(pattern_2,string)
# 获取匹配结果
if match_2:
    print(match_2)
    print(match_2.group())
    print(match_2.group(1))
else:
    print("No match!!")

