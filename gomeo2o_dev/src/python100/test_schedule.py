#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_schedule.py
@time: 2016/10/20 下午5:17
"""


import schedule
import time


def job():
    print("I'm working...")
def job1():
    print("Job1 working...")

def run():
    schedule.every(1).seconds.do(job1)
    schedule.every(0.1).seconds.do(job)
    schedule.every(10).minutes.do(job1)
    schedule.every().hour.do(job1)
    schedule.every().day.at("10:30").do(job1)
    schedule.every().monday.do(job1)
    schedule.every().wednesday.at("13:15").do(job1)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    run()

"""
$ pip install schedule

python 版本的定时调度

注意：
schedule.every().hour.do(job)
调度器开始工作后1个小时开始执行 job

"""
