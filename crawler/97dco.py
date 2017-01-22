#-*- coding:utf-8 -*-
import requests
import re
import json

# 入口页的url
url = 'http://www.97doc.com'
# 伪装成浏览器
header = {
    'Host': 'www.97doc.com',
    'Referer': 'http://www.97doc.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}
s = requests.session()
def get_city_list():
    response = s.get(url, headers=header)
    html = response.text
    #rule = '<a href="http://.*?.58.com/" onclick="co\(\'(.*?)\'\)">(.*?)</a>'
    rule = '<meta name="keywords" content="(.*?)"/>'
    content = re.compile(rule, re.S).findall(html)
    for i in content:
        print i
    print '97doc业务为:'
    print json.dumps(content).decode('raw_unicode_escape')


if __name__ == '__main__':
    get_city_list()

