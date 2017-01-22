#-*- coding:utf-8 -*-
import json
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import os,sys,re,jenkins
reload(sys)
sys.setdefaultencoding('UTF-8')
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
DATA_PATH = BASE_PATH + os.path.sep + 'scripts' + os.path.sep
import time,configparser,jenkins
#def read_wiki(result_dict):
def read_wiki():
    #生成configparser对象
    deploy_order = configparser.ConfigParser()
    deploy_order.read('online_list.conf')#所有项目清单
    #赋值两个空列表
    deploy, plan = [], []
    plan_order=[]
    #得到模块名
    for section in deploy_order.sections():
        #-options(section) 得到该section的所有option(把模块下的所有所有项目赋值到x
        #在加进空列表 )
        [deploy.append(x) for x in deploy_order.options(section)]
    print 'deploy 列表'
    print json.dumps(deploy)
    #循环deploy_order列表(所有的项目)，一个一个取值
    for order in deploy:
        with open(DATA_PATH+'20161101184654','rb') as op:
            data=op.read()
            data=data.decode('utf-8')
            #print(data)
            #data=data.decode('utf-8')
            if order in data:
                plan.append(order)
            else:
                print("%s没找到"%order)
    #'comx-bs'不发
    for line in plan:
        if line == 'comx-bs':
            plan.remove('comx-bs')
        else:
            pass
    #得到发版项目列表
        print json.dumps(plan)
    for plan_name in plan:
         with open(DATA_PATH+'20161101184654','rb') as op:
            data=op.read()
            data=data.decode('utf-8')
            res_th = plan_name+'/(.*?)</td>'
            m_th = re.findall(res_th,data,re.S)
            #print(m_th)
            plan_order.append(m_th)
    #得到发版项目版本号列表
    print json.dumps(plan_order)
    #版本号二次整理
    plan_order2=[]
    for line in plan_order:
        #如果列表有多个参数，就取最新的
        if len(line)>1:
            plan_order2.append(line[-1])
        else:
            plan_order2.append(line)
    print json.dumps(plan_order2)
    plan_order3=[]
    for x in plan_order2:
        #将列表准换成字符串
        x=''.join(x)
        #匹配数字.数字的格式
        plan_order3.append(re.findall(r'\d.*\d.*\d',x))
    print json.dumps(plan_order3)
    #将列表转换成字符串
    plan_order4=[]
    for i in plan_order3:
        i=''.join(i)
        plan_order4.append(i)
    #将两个列表组成字典
    print json.dumps(plan_order4)
    dict_out_put = dict(zip(plan, plan_order4))
    print json.dumps(dict_out_put)
read_wiki()


