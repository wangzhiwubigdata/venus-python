#!/usr/bin/python
# -*- coding: utf-8 -*-

from kazoo.client import KazooClient
import redis
import config

class ZkClient:
    def __init__(self):
        self.zkclient = KazooClient(hosts=config.configs['zkaddress'], read_only=True, timeout=30, connection_retry=3)
        self.zkclient.start()

    def zk_stop(self):
        self.zkclient.stop()

    def get_client(self):
        return self.zkclient


class RedisClient:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host=config.configs['redisaddress'], port=6379, db=0)

    def get_redisclient(self):
        return self.redis_client
