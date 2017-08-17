# encoding: utf-8
#!/usr/bin/python2.7
import json
from itertools import groupby

import easygui
import requests
import time


url = 'http://yfcp807.com/tools/ssc_ajax.ashx?A=GetLotteryOpen&S=yfvip&U=132974199455'
header = {
    'Host': 'yfcp807.com',
    'Origin': 'http://yfcp807.com',
    'Referer': 'http://yfcp807.com/lottery/K3/1407',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie':'route=134217aa4e8e12a08665fba45d9ec79f; token=94b04c7bfa75e1886efde9beaee135e4; random=2580; C_SessionId=e55fa638-1bcc-4d49-aca3-3fd4cabb83a5',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
postdata = {
    'A': 'GetLotteryOpen',
    'S': 'yfvip',
    'U':'132974199455',
    'Action' : 'GetLotteryOpen',
    'LotteryCode': 1407,
    'IssueNo': 0,
    'DataNum': 5,
    'SourceName': 'PC'
}
def log_in():
    pass


def get_data():
    addslist = []
    dxlist = []
    arrayList = []
    response = requests.post(url,postdata,headers=header)
    html = response.text
    jsons = json.loads(html)
    ar = jsons.get('BackData')
    for key in ar:
        sv = key['LotteryOpen'].split(',')
        adds = sum(int(a) for a in sv)
        arrayList.append(adds)
        ds = adds % 2
        dx = adds // 11

        addslist.append(dx)
        dxlist.append(ds)
    print '最近6次的原值为： ' + str(arrayList)
    return addslist,dxlist,arrayList


def get_max_length(addslist,dxlist,originlist):
    #print max(len(list(g)) for k, g in groupby(list) if k == 1)
    list = addslist
    result = {}
    tmp = None
    for i in list:
        if not result.has_key(i):
            # 新出现的值为1
            result[i] = {'tmpcount': 1, 'maxcount': 1}
        else:
            if i == tmp:
                # 同上一次相同,tmpcount数字加一,同时更新maxcount
                result[tmp]['tmpcount'] = result[tmp]['tmpcount'] + 1
                if result[tmp]['maxcount'] < result[tmp]['tmpcount']:
                    result[tmp]['maxcount'] = result[tmp]['tmpcount']
            else:
                # 如果不同，上次数字的tmpcount归零，这次的数字的tmpcount归一
                result[i]['tmpcount'] = 1
                result[tmp]['tmpcount'] = 0
        tmp = i

    for j, k in result.items():
        print '数字' + str(j) + '出现的最大连续次数为' + str(k['maxcount'])



if __name__ == '__main__':
    while 1==1:
        print 'waiting .................'
        time.sleep(30)

        daxiaolist, danshuanglist,originlist = get_data()
        print 'big small:' + str(daxiaolist)
        print 'pos pre:' + str(danshuanglist)

        if len(list(set(daxiaolist))) == 1:
            easygui.msgbox(str(originlist), u'注意!')
            #easygui.msgbox(u'6个大小连续出现了', u'注意!')
        if len(list(set(danshuanglist))) == 1:
            easygui.msgbox(str(originlist), u'注意!')
            #easygui.msgbox(u'6个单双连续出现了', u'注意!')
    print '------------------------------NEXT------------------------------'





###############################测试最长字串################################
    #addslist, dxlist, arrayList = get_data()
    #get_max_length(addslist, dxlist, arrayList)



