# -*- coding: utf-8 -*-

# 写方法
with open('./file.txt', 'a') as file3:
    file3.write('hello world')

# 常规读取方法
try:
    file = open('./file.txt', 'r')
    print file.read()
finally:
    if file:
        file.close()

# with 方法 自动调用close 方法
with open('./file.txt', 'r') as file2:
    print file2.readline()