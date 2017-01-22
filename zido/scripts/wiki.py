# -*- coding: utf-8 -*-
import os,sys
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
import time
from http.u_http import HttpClient
from data.read_wiki import read_wiki
import json
#from User import User
httpClient = HttpClient()
import requests

def login(url,body,url1):
    s=requests.post(url=url,data=body,allow_redirects=False)
    #print(s.status_code)
    JSESSIONID=s.cookies['JSESSIONID']
    cks={
        'JSESSIONID':JSESSIONID
    }
    res=requests.get(url1,cookies=cks)
    res.encoding='utf-8'
    #接受发版列表
    faban_list=read_wiki(res.text)

def run(pageId):
    pageId=str(pageId)
    url = "http://wiki.intra.gomeplus.com/pages/viewpage.action?"+'pageId='+pageId
    print(url)
    url1='http://wiki.intra.gomeplus.com/dologin.action'
    body={
        'os_username':'wangsen',
        'os_password':'WANGs1.',
        'login':'登录',
        'os_destination':''
    }
    login(url1,body,url)
    # print(value)
    # #body如果需要就填上数据如果不需要就置空，body={}
    # body = {}
    #
    # #接口访问的方式 get或post
    # u_method = "get"
    #
    # #处理v2接口需要在header里加“Accept”
    # header = {}
    # # A451ED019F130356AEF51CB768540B86
    # #value = "A3B6F39B9F9925E6BD5D61280A787892"
    # header["Content-Type"] = "application/x-www-form-urlencoded"
    # header["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
    # cookie='JSESSIONID='+value+'; doc-sidebar=300px;confluence.list.pages.cookie=list-content-tree; \
    # confluence.browse.space.cookie=space-pages;Hm_lvt_4d914dda44888419a4588c6a4be8edcc=1473650378'
    # print(cookie)
    # header['Cookie'] =cookie
    # # if ApiIsV2(url):
    # #     header["Content-Type"] = "application/x-www-form-urlencoded"
    # #     header["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
    #
    # #verify为验证项列表，用于检查返回内容中的关键字
    # verify = []
    #
    # postData={}
    # #执行被测接口
    # result_dict = httpClient.api_verify(url,postData,u_method,header,verify,body)
    # print(result_dict)
    #接受发版列表
    #faban_list=read_wiki(result_dict)





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
