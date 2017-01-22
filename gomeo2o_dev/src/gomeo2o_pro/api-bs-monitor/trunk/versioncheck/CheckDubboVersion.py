#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import urllib
from urlparse import urlparse
from kazoo.client import KazooClient
import sys
import logging

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)

#VENUS_DUBBO_COMSUMER = "venus-item-dubbo-consumer.xml"
#VENUS_DUBBO_PROVIDER = "venus-item-dubbo-provider.xml"
VENUS_DUBBO_COMSUMER = sys.argv[1]
VENUS_DUBBO_PROVIDER = sys.argv[2]


# 获取jar包中的版本号
def getJarDubboService(type, dubboFlie):  # reference,service
    interface_dict = {}
    DOMTree = xml.dom.minidom.parse(dubboFlie)
    tree = DOMTree.documentElement
    dubbo_reference = tree.getElementsByTagName('dubbo:' + type)
    for ref in dubbo_reference:
        if ref.hasAttribute("version") and ref.hasAttribute('interface'):
            interface_dict[ref.getAttribute("interface")] = ref.getAttribute("version")
    return interface_dict


def getServices(interface, type, zk):
    if zk.exists("/dubbo/" + interface + "/" + type):
        children = zk.get_children("/dubbo/" + interface + "/" + type)
        services = [urllib.unquote(data) for data in children]
        urls = [urlparse(service) for service in services]
        for index in range(len(urls)):
            querys = []
            queryDict = {}
            querys = urls[index].query.split('&')
            map(lambda x: queryDict.setdefault(x.split('=')[0], x.split('=')[1]), querys)
            urls[index].queryDict = queryDict
        return urls


if __name__ == "__main__":


    print "-------------------starting------------------------"
    zk = KazooClient(hosts='10.125.2.9:2181', read_only=True, timeout=30, connection_retry=3)
    zk.start()
    venus_xml_reference = getJarDubboService('reference', VENUS_DUBBO_COMSUMER)
    venus_xml_service = getJarDubboService('service', VENUS_DUBBO_PROVIDER)
    # 1、检查提供者
    for key in venus_xml_reference.keys():
        check_flag = 0;
        zkServices = getServices(key, 'providers', zk)
	if ( zkServices is not None ):
        	for zkService in zkServices:
	    		#print key+':'+venus_xml_reference[key]
            		if (zkService.queryDict.get('version') == venus_xml_reference[key]):
                		check_flag = 1

        if ( check_flag == 0 ):
		print key+':'+venus_xml_reference[key]+'--> NOT HAVE PROVIDER ! ! !'
    zk.stop()
    print "-------------------ending------------------------"
