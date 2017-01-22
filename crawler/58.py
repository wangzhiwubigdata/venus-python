# encoding: utf-8

import requests
import re
import json
# 入口页的url
url = 'http://www.gaokaopai.com/paihang-otype-2.html?f=1&ly=bd&city=&cate=&batch_type='

# 伪装成浏览器
header = {
    'Host': 'www.gaokaopai.com',
    'Referer': 'https://www.baidu.com/link?url=Q-Bj_e-T7CK9gOsx8fbcCMBOzt-3CfkdN5yIjjlhG0G0rVOpkQNVdhIosofTEYLadvuNDJxLPlosSLs4I8ccZzzui5CgtUrRF6anj8qe7cA9h_c7HbQNLA-JIdqTaa6W&wd=&eqid=e8480b110002154f00000002581c44d5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}
s = requests.session()
def get_city_list():
    """
<a href="http://hz.58.com/" onclick="co('hz')">杭州</a>
<a href="http://www.gaokaopai.com/daxue-jianjie-2216.html" target="_blank">清华大学</a></td>
<td class="t3">98.5</td>
<td class="t2"><a href="http://www.gaokaopai.com/daxue-jianjie-477.html" target="_blank">北京大学</a></td>
<td class="t3">(.*?)</td>
    """
    response = s.get(url, headers=header)
    html = response.text
    print html
    #    rule = '<a href="http://.*?.58.com/" onclick="co\(\'(.*?)\'\)">(.*?)</a>'
    rule1 = '<a href="http://www.gaokaopai.com/daxue-jianjie-\d+.html" target="\_blank">(.*?)</a></td>'
    schools = re.compile(rule1, re.S).findall(html)
    print json.dumps(schools).decode('raw_unicode_escape')
    rule2 = '<td class="t3">(\d+.\d+)</td>'
    points = re.compile(rule2,re.S).findall(html)
    print points
    #result = dict(map(lambda x,y:[x,y], schools,points))
    import collections
    result = collections.OrderedDict((zip(schools[::1],points)))
    print '排名前25的让学校和得分如下：'
    print json.dumps(result, indent=4).decode('raw_unicode_escape')


if __name__ == '__main__':
    get_city_list()
