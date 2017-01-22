#!/usr/bin/python
# -*- coding: UTF-8 -*-

import jenkins
import time
import configparser

#配属文件信息（地址，登陆用户名，登陆token）
JKS_CONFIG = {
    'jenkins_server_url': 'http://jks.pre.gomeplus.com:8787/jenkins',
    'user_id': 'admin',
    'api_token': '9d9fe1b771538d889550aa686d526ee2'
}

#实例化jenkins对象，连接远程的jenkins master server
server = jenkins.Jenkins(JKS_CONFIG['jenkins_server_url'], username=JKS_CONFIG['user_id'],
                         password=JKS_CONFIG['api_token'], timeout=3000)

#收取get_runing_build_status 将项目名称，和现在的构建编号传入
def get_runing_build_status(name, num):
    try:
        #判断job名为job_name的job的某次构建是否还在构建中
        #server.get_build_info(job_name,build_number)['result']　
        stat = server.get_build_info(name, num)['building']
    except Exception:
        print( '    ...waiting...')
        stat = True
    return stat

#依次传入的是项目名称，版本号字典
def build_job(name, parameter):
    #打印出项目
    input("-----确认发%s，请回车-----" % name)

    #获取job名为job_name的job的最后次构建号
    last_build_num = server.get_job_info(name)['lastBuild']['number']

    print ('[%s]开始构建....' % name)
    '''
    #构建job名为job_name的job（不带构建参数）
    # 构建 #构建job名为job_name的job（parameters是我穿进来的构建参数）
    #String参数化构建job名为job_name的job, 参数param_dict为字典形式，\
    # 如：param_dict= {"param1"：“value1”， “param2”：“value2”}
　　#server.build_job(job_name, parameters=param_dict)
    '''
    server.build_job(name, parameters=parameter)

    #调用get_runing_build_status 将项目名称，和现在的构建编号传入
    while get_runing_build_status(name, last_build_num + 1):
        print( '    ...building...')
        time.sleep(5)
    #获取job名为job_name的job的某次构建的执行结果状态
    is_success = server.get_build_info(name, last_build_num + 1)['result']
    print ('[%s]构建结束，构建结果: 【%s】' % (name, is_success))
    return is_success

#定了主程序（面向对象）
class PlanList:
    #生成config对象
    deploy_order = configparser.ConfigParser()
    deploy_list = configparser.ConfigParser()

    #初始化
    def __init__(self):
        #用config对象读取配置文件
        #read(filename) 直接读取ini文件内容
        self.deploy_order.read('online_list.conf')#所有项目清单
        self.deploy_list.read('deployList.conf')#发版列表

    def get_plan_dict(self):
        #赋值两个空列表
        deploy_order, plan_order = [], []
        #以列表形式返回所有的section
        #-sections() 得到所有的section，并以列表的形式返回
        #section=模块名称

        #得到模块名
        for section in self.deploy_order.sections():
            #-options(section) 得到该section的所有option(把模块下的所有所有项目赋值到x
            #在加进空列表 )
            [deploy_order.append(x) for x in self.deploy_order.options(section)]
        print(deploy_order)

        #循环deploy_order列表(所有的项目)，一个一个取值
        for order in deploy_order:
            #如果发版配置文件里的项目存在所有项目配置文件里（这里是按照所有项目配置里的项目排序的）
            if self.deploy_list.has_option('projects', order):
                print(order)
                #指定section=模块，option=项目   读取值=版本号
                order_version = self.deploy_list.get('projects', order)
                print(order_version)
                #定义字典 赋值版本号
                param_dict = {"VERSION": order_version}
                #循环掉build_job方法（往里面穿项目名称，版本字典）
                while build_job(order, param_dict) != 'SUCCESS':
                    input_str = input("发版失败，输入【K】跳过,否则重发此项目:")
                    if 'K' == input_str:
                        break
                #发版项目配置文件里面删除这个项目
                self.deploy_list.remove_option('projects', order)
        #如果发版配置文件'projects'下面还有项目
        if len(self.deploy_list.options('projects')) > 0:
            print ('下列工程没有发版')
            #打印出没有发办的项目名
            print (self.deploy_list.options('projects'))


if __name__ == '__main__':
    plane = PlanList()
    plane.get_plan_dict()
