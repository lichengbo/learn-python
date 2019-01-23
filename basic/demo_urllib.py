# -*- coding: utf-8 -*-
import urllib
import urllib2

url = 'http://www.baidu.com'

# 读页面
request = urllib2.Request(url)
response = urllib2.urlopen(request)
# print response.read()

# 设置user agent
url = 'http://www.baidu.com/s'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
values = {'wd': '搜索测试'}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
print response.read()

# 