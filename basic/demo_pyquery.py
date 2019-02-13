# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
response = pq("https://www.baidu.com")
# print response
print response('a').text()