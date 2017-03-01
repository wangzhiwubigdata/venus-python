#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
from tarutils import TarUtil
from collections import OrderedDict

import config


class PlanList:
    conf = ConfigParser.ConfigParser(dict_type=OrderedDict)
    conf_project = ConfigParser.ConfigParser(dict_type=OrderedDict)

    def __init__(self):
        self.conf.read('config/online_list.conf')
        self.conf_project.read('config/reading_deploy.conf')

    def get_plan_dict(self):
        deploy_order, plan_order = [], []
        for section in self.conf.sections():
            [deploy_order.append(x) for x in self.conf.options(section)]
        print deploy_order
        for order in deploy_order:
            if self.conf_project.has_option('venus', order):
                # 使用python下载并解压文件(原来调shell)
                order_version = self.conf_project.get('venus', order)
                print '获取工程：', order, order_version
                TarUtil().get_project(order, order_version)
                plan_order.append(order + '=' + order_version)
        print '=====发版顺序===='
        print plan_order
        print '========end========='


if __name__ == "__main__":
    print  config.configs['base'].get('nginx_url')
