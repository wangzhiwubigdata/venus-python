# -*- coding: utf-8 -*-
import os
import sys

from gomeo2o_dev.src.zidongfaban.http.u_http import HttpClient

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

#from User import User
httpClient = HttpClient()
import requests

def login(url,body):
    s=requests.post(url,data=body)
    print(s.cookies)
    # value=s.cookies['JSESSIONID']
    # print(value)
    # return value
    #print(s.cookies)
    #value=s.cookies[""]
    # url2='http://wiki.intra.gomeplus.com/'
    # s1=requests.get(url2)
    # print(s1.cookies)
    #return s

def run(pageId):
    pageId=str(pageId)
    url1='http://wiki.intra.gomeplus.com/dologin.action'
    body={
        'os_username':'wangsen',
        'os_password':'WANGs1.',
        'login':'登录',
        'os_destination':''
    }
    # value = login(url1,body)
    # print(value)
    url = "http://wiki.intra.gomeplus.com/pages/viewpage.action?"+'pageId='+pageId
    print(url)
    #body如果需要就填上数据如果不需要就置空，body={}
    body = {}

    #接口访问的方式 get或post
    u_method = "get"

    #处理v2接口需要在header里加“Accept”
    header = {}
    # A451ED019F130356AEF51CB768540B86
    value = "A3B6F39B9F9925E6BD5D61280A787892"
    header["Content-Type"] = "application/x-www-form-urlencoded"
    header["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
    cookie='JSESSIONID='+value+'; doc-sidebar=300px;confluence.list.pages.cookie=list-content-tree; \
    confluence.browse.space.cookie=space-pages;Hm_lvt_4d914dda44888419a4588c6a4be8edcc=1473650378'
    print(cookie)
    header['Cookie'] =cookie
    # if ApiIsV2(url):
    #     header["Content-Type"] = "application/x-www-form-urlencoded"
    #     header["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"

    #verify为验证项列表，用于检查返回内容中的关键字
    verify = []

    postData={}
    #执行被测接口
    result_dict = httpClient.api_verify(url,postData,u_method,header,verify,body)
    #接受发版列表
    faban_list=read_wiki(result_dict)





#判断是不是v2接口
# def ApiIsV2(url):
#     if "v2" in url:
#         return True
#     else:
#         return False

#前提操作
# def preStep(self):
#     "前提操作"
#     url = ""
#     postData = {}
#     u_method = "get"
#     header = {}
#     verify = []
#
#     response = httpClient.api_request(url, postData, u_method, header, verify)
#     return response

    # #将公参和必填参数组合
    # def sign_str(self,data,isV2=False):
    #     publicParaV1 = {
    #                "ip":"0.0.0.0",
    #                "appType":"1",
    #                "clientOsVersion":"8.4",
    #                "sortType":"0",
    #                "pubPlat":"0120102002000000",
    #                "appVersion":"v1.0.2.33",
    #                "latitude":"39.964707",
    #                "otherDevInfo":"otherDevInfo",
    #                "netType":"3G",
    #                "numPerPage":"5",
    #                "devId":"0",
    #                "clientOs":"1",
    #                "mac":"00000000",
    #                "lastRecordId":"0",
    #                "longitude":"116.47308",
    #                "pageNum":"1",
    #                "order":"2",
    #                "phoneType":"iPhone"
    #                }
    #
    #     publicParaV2 = {
    #                 "integrity":"full",
    #                 "device":"iOS/9.2.1/iPhone/IPhone12345678",
    #                 "app":"001/1111111111111",
    #                 "appVersion":"1.0.1",
    #                 "net":"",
    #                 "accessToken":"",
    #                 "traceId":"",
    #                 "jsonp":""
    #                 }
    #     if isV2:
    #         dictMerged = dict(data, **publicParaV2)
    #     else:
    #         dictMerged = dict(data, **publicParaV1)
    #
    #     return dictMerged


if __name__ == "__main__":

    pageId=input('wiki_number:')
    run(pageId)
