#!/bin/pathon
# -*- coding: utf-8 -*-
import pymysql.cursors
import re

connection = pymysql.connect(
    host='10.125.31.220',
    user='',
    password='',
    db='bs_admin_recharge',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)


def select_all(connection):
    with connection.cursor() as cursor:
        sql = "SELECT id, pid, name, level FROM gome_recharge_address WHERE level = 2 "
        cursor.execute(sql)
        results = cursor.fetchall()
        return results


# TODO 异常处理
def do_insert(connection, datas):
    with connection.cursor() as cursor:
        sql = "INSERT INTO gome_recharge_mobile_info (mobile,province,city,mno) VALUES(%s,%s,%s,%s)"
        cursor.executemany(sql, datas)
        connection.commit()


def getcity_no(data, results):
    city, province = None, None
    if "重庆" == data[1]:
        city = 74010000
        province = 74000000
    if "内蒙古" == data[1]:
        city = 15990000
        province = 15000000
    if city is None:
        for result in results:
            if re.match(r'^' + data[2], result['name']):
                city, province = result['id'], result['pid']
                break
    if city is None:
        for result in results:
            if re.match(r'^' + data[1] + '省其他城', result['name']):
                city, province = result['id'], result['pid']
                break
    return city, province


# 开始
results = select_all(connection)
with open('C:/Users/zhaozhou/Desktop/admin/number.txt', 'r', encoding='utf-8') as f:
    print ('开始导入数据....')
    params = []
    for line in f.readlines():
        data = []
        data = line.strip().split("\t")
        city, province = getcity_no(data, results)
        if province == 0:
            print (data[2], data[1], data[0], "province编码0")

        if city is None:
            print (data[2], data[1], data[0], "未找到编码")
        else:
            param = [int(data[0]), int(province), int(city), data[3]]
            params.append(param)

        if (len(params) == 3000):
            do_insert(connection, params)
            params = []

    print("最后导入：", len(params))
    do_insert(connection, params)
    connection.close()
    print ("导入完毕")
