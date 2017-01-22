# -* - coding: UTF-8 -* -
import urllib2, urllib
import traceback
#from utils.loggerInfo import logger
import socket
import timeit
import time
import json
from urllib import addinfourl

import sys
import httplib
import cookielib
stdout = sys.stdout
stderr = sys.stderr
stdin = sys.stdin
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = stdout
sys.stderr = stderr
sys.stin = stdin


class HttpClient():
    """docstring for HttpClient"""
    #cookie：是否需要cookie，flag：0-保存cookie，1-读取cookie
    def __init__(self, cookie=False,flag=0):
        self.cookie = cookie
        self.saveOrRead = flag
        filename = "E:/tmp/oa_cookie.txt"
        if self.cookie:
            if self.saveOrRead == 0:#写cookie
                print ""
                self.cookieFile = cookielib.MozillaCookieJar(filename)
            elif self.saveOrRead ==1:#读cookie
                print ""
                self.cookieFile = cookielib.MozillaCookieJar()
                self.cookieFile.load(filename,ignore_discard=True, ignore_expires=True)
            
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieFile))
        else:
            self.opener = urllib2.build_opener()
            

    def __addGETdata(self, url, data):
        "生成get数据"
        if data is None:
            return url
        elif '?' in url:
#             print url + '&' + urllib.urlencode(data)
            return url + '&' + urllib.urlencode(data)
        else: 
#             print "--------------"
#             print url + '?' + urllib.urlencode(data)
#             print "--------------"
            return url + '?' + urllib.urlencode(data)
#             return url + '?' + str(data)
    
    def __getReq(self, url, data=None, header=None):
        "组合request数据包"
        req = urllib2.Request(url)
        
        req.add_data(data)
        if header is not None:
            for k_key in header:
                req.add_header(k_key, header[k_key])
        return req
    
    def __getPutReq(self, url, body, header=None):
        "组合request数据包,put请求"
        #此处为对body是否为空进行判断，可能会出问题，有时间测试 一下
        jdata = json.dumps(body)
        
        req = urllib2.Request(url,jdata)
        if header is not None:
            for k_key in header:
                req.add_header(k_key, header[k_key])
        return req

    def sendGetRequest(self, url, data=None, headers=None):
        "发GET请求"
        
        try:
            url = self.__addGETdata(url, data)
        except Exception as e:
            #logger.error(traceback.format_exc())
            print(e)
#         print url
        req = self.__getReq(url, header=headers)
        try:
            fb = self.opener.open(req,timeout=10)
        except urllib2.HTTPError, e:
            raise e
        except urllib2.URLError, e:
            raise e

        return fb

    def sendPostRequest(self, url, data=None, headers=None,body=None):
        "发POST请求"
        if body is not None and len(body)>0:
            if data:
                try:
                    url = self.__addGETdata(url, data)
                except Exception as e:
                    #logger.error(traceback.format_exc())
                    print(e)
#         print url
            req = self.__getPutReq(url, body, header=headers)
            req.get_method = lambda: "POST"
            try:
                fb = urllib2.urlopen(req)
#                 fb = self.opener.open(req,timeout=30)
                if self.cookie and self.saveOrRead == 0:
                    self.cookieFile.save(ignore_discard=True, ignore_expires=True)
            except urllib2.HTTPError, e:
                raise e
            except urllib2.URLError, e:
                raise e
            except Exception ,e:
                raise e
    
            return fb
        else:    
            if data:
                try:
                    data = urllib.urlencode(data)
                except Exception as e:
                    #logger.error(traceback.format_exc())
                    print(e)

                
            req = self.__getReq(url, data, header=headers)
            
            try:
                fb = self.opener.open(req,timeout=30)
                if self.cookie:
                    self.cookieFile.save(ignore_discard=True, ignore_expires=True)
            except urllib2.HTTPError, e:
                raise e
            except urllib2.URLError, e:
                raise e
    
            return fb

    def sendPutRequest(self, url, data=None, headers={},body={}):
        "发put请求"
        if data:
            try:
                url = self.__addGETdata(url, data)
            except Exception as e:
                #logger.error(traceback.format_exc())
                print(e)
#         print url
        req = self.__getPutReq(url, body, header=headers)
        req.get_method = lambda: "PUT"
        try:
            fb = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            raise e
        except urllib2.URLError, e:
            raise e

        return fb
    
    def sendDeleteRequest(self, url, data=None, headers={},body={}):
        "发delete请求"
        if data:
            try:
                url = self.__addGETdata(url, data)
            except Exception as e:
                #logger.error(traceback.format_exc())
                print(e)
        print (url)
        req = self.__getPutReq(url, body, header=headers)
        req.get_method = lambda: "DELETE"
        try:
            fb = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            raise e
        except urllib2.URLError, e:
            raise e

        return fb
    
    def api_request(self,url,data=None,u_method="GET",header=None,verify=None,body=None):
        "处理请求，返回原始json串"
        try:
            if u_method.lower() == 'get':
                ret = self.sendGetRequest(url, data, header)
            elif u_method.lower() == 'post':
                ret = self.sendPostRequest(url, data, header,body)
            elif u_method.lower() == 'put':
                ret = self.sendPutRequest(url, data, header,body)
            elif u_method.lower() == 'delete':
                ret = self.sendDeleteRequest(url, data, header)
            return ret#json.loads(ret.read())#.decode('utf-8')
        except Exception as e:
            #logger.error("访问url=%s时出错:%s"%(url,str(e)))
            raise e
    
        
    #success: 0-成功 -1-失败
    #error: 0表示没有
    #http_code: -1没有
    def api_verify(self,url, data = None, u_method="GET", header=None, verify=None,body=None):
        "处理请求, 数据持久化，返回格式化结果"
        result_dict = {}
        
#         result_dict['param_json'] = json.dumps(data)
        result_dict['call_time'] = str(int(time.time()))#str(int(timeit.default_timer()))
        try:
            begin = timeit.default_timer()
            if u_method.lower() == 'get':
                ret = self.sendGetRequest(url, data, header)
            elif u_method.lower() == 'post':
                ret = self.sendPostRequest(url, data, header,body)
            elif u_method.lower() == 'put':
                ret = self.sendPutRequest(url, data, header,body)
            elif u_method.lower() == 'delete':
                ret = self.sendDeleteRequest(url, data, header)
                
            end = timeit.default_timer()
            result_dict['http_code'] = ret.code
            if ret.code != 200:
                #客户端请求接口错误
                result_dict['error_code'] = 0
                result_dict['success'] = -1
                result_dict['response_time'] = 0
            else:
                res_result = ret.read().decode('utf-8')
                result_dict['return_text'] = res_result
                count = 0
                #解析返回结果。当接口为h5页面时，解析结果会报错，在此处理一下。
                try:
                    data = json.loads(res_result)
                except Exception as e3:#h5页面，No JSON object could be decoded
#                     print e3
                    if "<html" in res_result:
                        result_dict['success'] = 0
                        result_dict['error_code'] = 0
                        result_dict['response_errortext'] = "成功"
                    else:
                        result_dict['success'] = -1
                        result_dict['error_code'] = 500
                        result_dict['response_errortext'] = res_result[0:300]
                    
                    result_dict['response_time'] = end-begin
                    
                else:#普通BS接口，非h5
                    if data.has_key("success") and data.has_key("code"):#v1接口
                        "v1接口"
                        if data['success']:
                            "成功"
                            if verify is not None:
                                for veri in verify:
                                    if veri in res_result:
                                        count+=1
                                if count == len(verify):
                                    result_dict['success'] = 0
                                else:
                                    result_dict['success'] = -1
                                    result_dict['response_errortext']="验证点失败"
                                    
                            else:
                                result_dict['success'] = 0
                        else:
                            "返回值success=false，需要进行业务判断"
                            
                            if verify is not None:
                                for veri in verify:
                                    if veri in res_result:
                                        count+=1
                                if count == len(verify):
                                    result_dict['success'] = 0
                                else:
                                    result_dict['success'] = -1
                                    result_dict['response_errortext']="验证点失败"
                                    
                            else:
                                result_dict['success'] = -1
                            
                        result_dict['error_code'] = data['code']
                        result_dict['response_time'] = end-begin
                        #当验证点都成功的时候，errortext就是请求返回内容
                        if not result_dict.has_key('response_errortext'):
                            result_dict['response_errortext'] = data['message']
                    else:
                        "v2接口"
                        if verify is not None:
                            for veri in verify:
                                if veri in res_result:
                                    count+=1
                            if count == len(verify):
                                result_dict['success'] = 0
                            else:
                                result_dict['success'] = -1
                                
                                
                        else:
                            result_dict['success'] = 0
                       
                        result_dict['http_code'] = 200
                        result_dict['error_code'] = 0
                        result_dict['response_time'] = end-begin
                        result_dict['response_errortext'] = None
                    
        except Exception, e:
            #print traceback.format_exc()
            result_dict['success'] = -1
            result_dict['http_code'] = -1
            result_dict['response_time'] = 0
            result_dict['return_text'] = None
            if isinstance(e, urllib2.HTTPError):
                #http错误
                result_dict['error_code'] = e.code
                rstr = e.read()
                print rstr
                result_dict['response_errortext'] = rstr
            elif isinstance(e, urllib2.URLError):
                #url错误
                print traceback.format_exc()
                result_dict['error_code'] = 601
                rstr = e.reason
                result_dict['response_errortext'] = rstr
            elif isinstance(e, socket.timeout):
                #超时
                result_dict['error_code'] = 602
                rstr = e
                result_dict['response_errortext'] = e
            else:
                #其他异常
                result_dict['error_code'] = 700
                rstr = str(type(e))+e.__str__()
                result_dict['response_errortext'] = rstr[0:1000]
        #返回数据
        return result_dict
