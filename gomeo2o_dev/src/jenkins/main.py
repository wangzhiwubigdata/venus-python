#!/usr/bin/python
# -*- coding: UTF-8 -*-

import jenkins
import time
import ConfigParser

JKS_CONFIG = {
    'jenkins_server_url': 'http://jks.pre.gomeplus.com:8787/jenkins',
    'user_id': 'admin',
    'api_token': '9d9fe1b771538d889550aa686d526ee2'
}

server = jenkins.Jenkins(JKS_CONFIG['jenkins_server_url'], username=JKS_CONFIG['user_id'],
                         password=JKS_CONFIG['api_token'], timeout=3000)


def get_running_build_status(name, num):
    try:
        stat = server.get_build_info(name, num)['building']
    except Exception:
        print '    ...waiting...'
        stat = True
    return stat


def build_job(name, parameter):
    build = raw_input("-----确认发%s，请回车-----,跳过请输入[N]" % name)
    if "N" == build:
        return

    # 获取上次构建编号
    last_build_num = server.get_job_info(name)['lastBuild']['number']

    print '[%s]开始构建....' % name

    # 构建
    server.build_job(name, parameters=parameter)

    while get_running_build_status(name, last_build_num + 1):
        print '    ...building...'
        time.sleep(5)

    is_success = server.get_build_info(name, last_build_num + 1)['result']
    print '[%s]构建结束，构建结果: 【%s】' % (name, is_success)
    return is_success


class PlanList:
    deploy_order = ConfigParser.ConfigParser()
    deploy_list = ConfigParser.ConfigParser()

    def __init__(self):
        self.deploy_order.read('online_list.conf')
        self.deploy_list.read('deployList.conf')

    def get_plan_dict(self):
        deploy_order, plan_order = [], []
        for section in self.deploy_order.sections():
            [deploy_order.append(x) for x in self.deploy_order.options(section)]

        for order in deploy_order:
            if self.deploy_list.has_option('projects', order):
                order_version = self.deploy_list.get('projects', order)
                param_dict = {"VERSION": order_version}

                while build_job(order, param_dict) != 'SUCCESS':
                    input_str = raw_input("发版失败，输入【K】跳过,否则重发此项目:")
                    if 'K' == input_str:
                        break

                self.deploy_list.remove_option('projects', order)

        if len(self.deploy_list.options('projects')) > 0:
            print '下列工程没有发版'
            print self.deploy_list.options('projects')


if __name__ == '__main__':
    plane = PlanList()
    plane.get_plan_dict()
