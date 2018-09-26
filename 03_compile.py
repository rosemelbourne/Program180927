import re

pattern = r"abcdef"
s = "abcdefghijklmnabcdef"

regex = re.compile(pattern)
l = regex.findall(s)
print(l)
print('=======================')


'''split'''
pattern = r"\s+"
s = "Hello  world nihao China"

regex = re.compile(pattern)
l = regex.split(s)
print("split():",l)
print('=======================')

# split(): ['Hello', 'world', 'nihao', 'China']


'''sub'''
pattern = r'\s+'
s = "Hello   world  nihao China"

regex = re.compile(pattern)
l = regex.sub("#",s,count=2)
print("sub():",l)
print('=======================')

l = regex.sub("#",s)
print("sub():",l)
print('=======================')

# sub(): Hello#world#nihao China
# sub(): Hello#world#nihao#China


'''subn'''
pattern = r'\s+'
s = "Hello   world  nihao China"

regex = re.compile(pattern)
l = regex.subn("#",s,count = 2)
print("subn():",l)
print('=======================')

l = regex.subn("#",s)
print("subn():",l)
print('=======================')

# subn(): ('Hello#world#nihao China', 2)
# subn(): ('Hello#world#nihao#China', 3)


'''finditer'''
pattern = r'\d+'
s = "现在是2018年9月25日17点10分"

regex = re.compile(pattern)
l = regex.finditer(s)
for i in l:
    print(i.group())


'''fullmatch'''
pattern = r'\w+'
s = "abcdef123#"

regex = re.compile(pattern)
l = regex.fullmatch(s)
print(l)

# None


# '''match() 只能匹配开始位置，等同于＾'''
pattern = r'foo'
s = "foo means function."

regex = re.compile(pattern)
l = regex.match(s)
print(l.group())


# '''search() 匹配任意位置，但只匹配一处'''
pattern = r'foo'
s = "Food or food means lots for me."

regex = re.compile(pattern)
l = regex.search(s)
print(l.group())