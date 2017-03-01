#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import urllib
from urlparse import urlparse
from client import ZkClient, RedisClient
import logging
import os
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)

zk = ZkClient().get_client
redis = RedisClient().get_redisclient()


class ZkOperate:
    def __init__(self, zkclient, redisclient):
        self.zkclient = zkclient
        self.redis_client = redisclient

    # 获取所有节点数据，存入redis
    def zk_to_redis(self, side):
        interfaces = self.zkclient.get_children("/dubbo")
        for interface in interfaces:
            # 获取data
            dubbo_url_list = self.zkclient.get_children("/dubbo/" + interface + "/" + side)
            if len(dubbo_url_list) == 0:
                continue
            # unquote(data)
            if side == "providers":
                services = [urllib.unquote(dubbo_url).replace("dubbo://", "http://") for dubbo_url in dubbo_url_list]
            else:
                services = [urllib.unquote(dubbo_url).replace("consumer://", "http://") for dubbo_url in dubbo_url_list]
            # to Object[]
            dubbo_urls = [urlparse(service) for service in services]
            for index in range(len(dubbo_urls)):
                query_dict = {}
                querys = dubbo_urls[index].query.split('&')
                map(lambda x: query_dict.setdefault(x.split('=')[0], x.split('=')[1]), querys)
                dubbo_urls[index].query_dict = query_dict
            # 存入redis
            for dubbo in dubbo_urls:
                app_detail = ''
                try:
                    app_detail = 'application:' + dubbo.query_dict.get('application') + ',flag:old'
                except Exception:
                    print dubbo.query_dict
                if not dubbo.query_dict.has_key('version'):
                    print 'dubbo:' + interface + '：这个接口没带版本号'
                    continue
                dubbo_redis_key = 'dubbo:' + interface + ':' + side + ':' + dubbo.query_dict['version']
                self.redis_client.sadd('dubboapp:' + dubbo.query_dict["application"] + ':old', dubbo_redis_key)
                self.redis_client.sadd(dubbo_redis_key, app_detail)


class FileOperate:
    # 获取jar包中的版本号

    def __init__(self, redisclient):
        self.redis_client = redisclient

    @staticmethod
    def dubbo_service_from_jar(key_word, dubbo_file):  # reference,service
        interface_dict = {}
        dom_tree = xml.dom.minidom.parse(dubbo_file)
        tree = dom_tree.documentElement
        dubbo_reference = tree.getElementsByTagName('dubbo:' + key_word)
        for ref in dubbo_reference:
            if ref.hasAttribute("version") and ref.hasAttribute('interface'):
                interface_dict[ref.getAttribute("interface")] = ref.getAttribute("version")
        return interface_dict

    # 获取列表中文件，获取版本号存入redis
    def files_to_redis(self, xml_files):
        for xml_file in xml_files:
            if xml_file.find('consumer') != -1:
                if re.match(r'.*/venus-.*servlet-.*\.xml', xml_file.replace('\\', '/')):
                    application = 'venus-servlet-api'
                else:
                    application = xml_file.replace('\\', '/').split('/')[-1].split('-dubbo')[0]
                    if "venus-admin" == application:
                        application = 'admin'
                    if 'venus-web' == application:
                        application = 'xpop'
                    if 'mars-o2mitem-pre' == application:
                        application = 'venus-origin-servlet'
                    if 'mars-o2mtrade-pre' == application:
                        application = 'venus-origin-servlet'
                    if "venus-user" == application:
                        application = 'venus_user'
                    if "venus-audit" == application:
                        application = 'venus-audit-web'

                interface_dict = self.dubbo_service_from_jar('reference', xml_file)
                for key in interface_dict.keys():
                    self.save_to_redis(key, application, 'consumers', interface_dict[key], 'new')

            else:
                application = xml_file.replace('\\', '/').split('/')[-1].split('-dubbo')[0]
                service_dict = self.dubbo_service_from_jar('service', xml_file)
                for key in service_dict.keys():
                    self.save_to_redis(key, application, 'providers', service_dict[key], 'new')

    def save_to_redis(self, key, application_name, silde, dubbo_version, flag):
        app_detail = 'application:' + application_name + ',flag:' + flag
        redis_dubbo_key = 'dubbo:' + key + ':' + silde + ':' + dubbo_version
        self.redis_client.sadd(redis_dubbo_key, app_detail)
        self.redis_client.sadd('dubboapp:' + application_name + ':' + flag, redis_dubbo_key)

    # 获取文件
    def list_consumer(self, folder, allfile):
        folders = os.listdir(folder)
        for name in folders:
            curname = os.path.join(folder, name)
            isfile = os.path.isfile(curname)
            if isfile:
                if curname.find("META-INF") != -1:
                    continue
                if re.match(r'.*(spring|config).*(provider|consumer)', curname):
                    allfile.append(curname)
            else:
                self.list_consumer(curname, allfile)
        return allfile


class RedisOperate:
    def __init__(self, redisclient):
        self.redis_client = redisclient

    # 打印
    def print_redis_data(self):
        keys = [self.redis_client.keys("dubbo:*")]
        for key in keys[0]:
            print self.redis_client.smembers(key)

    # 删除所有dubbo_key
    def del_dubbo_keys(self):
        keys = [self.redis_client.keys("dubbo*")]
        for key in keys[0]:
            self.redis_client.delete(key)

    # 检查消费者是否有对应提供者
    def chcek_consumers(self):
        consumers = self.redis_client.keys("dubbo:*consumers*")
        for consumer in consumers:
            if consumer.find('com.gome.io.facet') != -1:
                continue
            if consumer.find('gome.stat.facade') != -1:
                continue
            if len(self.redis_client.smembers(consumer.replace("consumers", "providers"))) == 0:
                apps = [x for x in self.redis_client.smembers(consumer) if x.find('consumer-gome') == -1]
                if len(apps) > 0:
                    consumer = consumer.split(':')[1] + ':' + consumer.split(':')[3]
                    print consumer, "【没有提供者】"
                    for app in apps:
                        print '\t', '-->', app
                    print ""

    # 删掉老版本服务
    def delall_oldapp(self):
        dubbo_data = self.redis_client.keys('dubbo:*')
        for dubbo_key in dubbo_data:
            app_sets = self.redis_client.smembers(dubbo_key)
            for s in app_sets:
                print s
                if s.split(':')[-1] == 'old':
                    self.redis_client.srem(dubbo_key, s)

    def del_old_service(self):
        new_apps = self.redis_client.keys('dubboapp:*:new')
        for new_app in new_apps:
            dubbo_interfaces = self.redis_client.smembers(new_app.replace('new', 'old'))
            for key in dubbo_interfaces:
                self.redis_client.srem(key, 'application:' + new_app.split(':')[1] + ',flag:old')


if __name__ == "__main__":
    redis = RedisClient().get_redisclient()
    redisOperate = RedisOperate(redis)
    redisOperate.del_old_service()
    redisOperate.chcek_consumers()
