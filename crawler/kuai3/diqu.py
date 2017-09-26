#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import json
import requests
import time
import itchat

districts = {
    '1402':u'安徽',
    '1406':u'北京',
    '1411':u'甘肃',
    '1403':u'广西',
    '1409':u'贵州',
    '1408':u'河北',
    '1405':u'湖北',
    '1401':u'江苏',
    '1404':u'吉林',
    '1410':u'上海'
}
def get_header(key):

    url = 'http://yfcp809.com/tools/ssc_ajax.ashx?A=GetLotteryOpen&S=yfvip&U=wchy563630987'

    headers = {
        'Host': 'yfcp809.com',
        'Origin': 'http://yfcp809.com',
        'Referer': 'http://yfcp809.com/lottery/K3/'+ str(key), #1407
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'route=134217aa4e8e12a08665fba45d9ec79f; token=94b04c7bfa75e1886efde9beaee135e4; random=2580; C_SessionId=e55fa638-1bcc-4d49-aca3-3fd4cabb83a5',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    postdata = {
        'A': 'GetLotteryOpen',
        'S': 'yfvip',
        'U': '132974199455',
        'Action': 'GetLotteryOpen',
        'LotteryCode': key, #1407
        'IssueNo': 0,
        'DataNum': 8,
        'SourceName': 'PC'
    }
    return url,headers,postdata

def log_in():
    itchat.auto_login(hotReload=True)



def get_dafa_data():
    url,headers,postdata = get_header(1407)
    print url,postdata,headers
    dsList = []
    dxlist = []
    arrayList = []
    response = requests.post(url, postdata, headers=headers)
    html = response.text
    jsons = json.loads(html)
    ar = jsons.get('BackData')
    for key in ar:
        sv = key['LotteryOpen'].split(',')
        adds = sum(int(a) for a in sv)
        arrayList.append(adds)
        ds = adds % 2
        dx = adds // 11

        dsList.append(ds)
        dxlist.append(dx)

    print '最近6次的值为： ' + str(arrayList)
    return dsList, dxlist

def send_msg(time,dis):
    users = itchat.search_friends(name='mapper')
    # 获取好友全部信息,返回一个列表,列表内是一个字典
    userName = users[0]['UserName']
    print dis + "-->" + str(time)
    itchat.send(dis + "-->" + str(time), toUserName=userName)

def send_msg_to_niexiong(time,dis):
    users = itchat.search_friends(name='nilxon')
    # 获取好友全部信息,返回一个列表,列表内是一个字典
    userName = users[0]['UserName']
    print dis + "-->" + str(time)
    itchat.send(dis + "-->" + str(time), toUserName=userName)
def send_msg_to_luxibo(time,dis):
    users = itchat.search_friends(name='luxibo')
    # 获取好友全部信息,返回一个列表,列表内是一个字典
    userName = users[0]['UserName']
    print dis + "-->" + str(time)
    itchat.send(dis + "-->" + str(time), toUserName=userName)

def get_other_data(key):
    url,headers,postdata = get_header(key)
    dsList = []
    dxlist = []
    arrayList = []
    response = requests.post(url, postdata, headers=headers)
    html = response.text
    jsons = json.loads(html)
    ar = jsons.get('BackData')
    for key in ar:
        sv = key['LotteryOpen'].split(',')
        adds = sum(int(a) for a in sv)
        arrayList.append(adds)
        ds = adds % 2
        dx = adds // 11

        dsList.append(ds)
        dxlist.append(dx)
    print '最近6次的值为： ' + str(arrayList)
    return dsList, dxlist






if __name__ == '__main__':

    #登录
    log_in()
    #开始循环
    while 1 == 1:


        print "start....."

        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print now
        for key in districts.keys():
            dslist, dxlist = get_other_data(key)
            print key
            print dxlist
            print dslist
            if len(list(set(dxlist))) == 1:
                send_msg(now,districts[key])
                send_msg_to_niexiong(now, districts[key])
                send_msg_to_luxibo(now,districts[key])
            if len(list(set(dslist))) == 1:
                send_msg(now,districts[key])
                send_msg_to_niexiong(now, districts[key])
                send_msg_to_luxibo(now, districts[key])

        time.sleep(300)

        print "-----------------------------NEXT---------------------------------"
