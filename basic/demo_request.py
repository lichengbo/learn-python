# -*- coding: utf-8 -*-
import requests
r = requests.get('https://aiui.iflyos.cn')
print type(r)
print r.status_code
print r.encoding
# print r.text
print r.cookies

# 请求接口
payload = {'key1': 'value1', 'key2': 'value2'}
r1 = requests.get('https://aiui.iflyos.cn/aiui/web/user/auth/userInformation', params=payload)
print r1.url
print r1.text