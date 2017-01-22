#-*- coding:utf-8 -*-
import os,sys,re
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
DATA_PATH = BASE_PATH + os.path.sep + 'scripts' + os.path.sep
import time
def read_wiki(result_dict):
    #发送时间
    timeStr = time.strftime("%Y%m%d%H%M%S", time.localtime())
    #标题
    subject = u"【今日发版内容】"+"_"+timeStr
    f=open(subject,"w")
    f.write(str(result_dict)+"\n")
    f.close()
    with open(DATA_PATH+subject,'rb') as op:
        data=op.read()
        # language = '''''<pre>*/*</pre>'''
        # #正则表达式获取<tr></tr>之间内容
        # res_tr = r'<tr>(.*?)</tr>'
        # m_tr =  re.findall(res_tr,language,re.S|re.M)
        allfinds2 = re.findall(r'<pre>(.*?)</pre>',data, re.S)
        print(allfinds2)




