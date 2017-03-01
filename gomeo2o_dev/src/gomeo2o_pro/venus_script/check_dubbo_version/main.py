#!/usr/bin/python
# -*- coding: utf-8 -*-
import planlist
from client import ZkClient, RedisClient
from operation import ZkOperate, RedisOperate, FileOperate
import config

if __name__ == "__main__":
    TMP = config.configs['tmp_dir']
    zk = ZkClient().get_client()
    redis = RedisClient().get_redisclient()
    redisOperate = RedisOperate(redis)
    zkOperate = ZkOperate(zk, redis)
    fileOperate = FileOperate(redis)

    print '-----1.下载解压-----'
    planlist.PlanList().get_plan_dict()

    print '-----2.清空redis---------'
    redisOperate.del_dubbo_keys()

    print '-----3.zk --- to----- redis'
    zkOperate.zk_to_redis('providers')
    zkOperate.zk_to_redis('consumers')

    print '-----4.文件中版本存redis----'
    allfile = []
    files = fileOperate.list_consumer(TMP, allfile)
    fileOperate.files_to_redis(files)

    print '-----5.检查没有提供者-----'
    redisOperate.chcek_consumers()

    print '-----6.结束灰度后检查没有提供者-----------'
    redisOperate.del_old_service()
    redisOperate.chcek_consumers()
    print '-----7.结束-------------'

    zk.stop()
