# -*- coding: utf-8 -*-
import re

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')

# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC!')

# 如果1匹配成功
if result1:
    # 使用Match获得分组信息
    print result1.group()
else:
    print '1匹配失败！'

# 如果2匹配成功
if result2:
    # 使用Match获得分组信息
    print result2.group()
else:
    print '2匹配失败！'

# 如果3匹配成功
if result3:
    # 使用Match获得分组信息
    print result3.group()
else:
    print '3匹配失败！'

# 如果4匹配成功
if result4:
    # 使用Match获得分组信息
    print result4.group()
else:
    print '4匹配失败！'

pattern = re.compile(r'\d+')
print re.findall(pattern, 'one1two2three3four4')

### 输出 ###
# ['1', '2', '3', '4']



# 修饰符
# re.I 使匹配对大小写不敏感
# re.L 做本地化识别（locale-aware）匹配
# re.M 多行匹配，影响 ^ 和 $
# re.S 使 . 匹配包括换行在内的所有字符
# re.U 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解

# 常用表达式
# 1、匹配email地址:
# [\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?
# 2、匹配网址URL：
# [a-zA-z]+://[^\s]*
# 3、匹配18位身份证号：
# ^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$
# 4、匹配年月日格式：
# ([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))
# 5、匹配整数：
# ^-?[1-9]\d*$
# 6、匹配正整数：
# ^[1-9]\d*$
# 7、匹配负整数：
# ^-[1-9]\d*$
# 8、匹配空白行：
# \n\s*\r