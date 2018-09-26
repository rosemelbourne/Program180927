import re

pattern = r'(?P<dog>ab)cd(?P<pig>ef)'
regex = re.compile(pattern)

# 获取match对象
match_obj = regex.search('abcdefghij')

print(match_obj.pos)            # 匹配目标字符串的开始位置
print(match_obj.endpos)         # 匹配目标字符串的结束位置

print(match_obj.re)             # 正则表达式
print(match_obj.string)         # 目标字符串

print(match_obj.lastgroup)      # 最后一组的组名
print(match_obj.lastindex)      # 最后一组是第几组
print('=======================')

print(match_obj.start())        # 匹配内容的开始位置
print(match_obj.end())          # 匹配内容的结束位置
print(match_obj.span())         # 匹配内容的起止位置

print(match_obj.group())        # 获取整个match对象的内容
print(match_obj.group(2))       # 获取第二个子组的匹配内容
print(match_obj.group('dog'))  # 获取dog子组的匹配内容

print(match_obj.groups())       # 获取每个子组的匹配内容
print(match_obj.groupdict())    # 获取捕获组字典

# 可能是前几行由于出错没打印，导致后几行打印不出来