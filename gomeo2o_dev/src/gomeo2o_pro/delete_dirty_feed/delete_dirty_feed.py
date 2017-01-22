import sys
import optparse
import contextlib
import time

import pymongo

class Executor(object):
    def __init__(self, args=None):
        self.options = self.parse_args(args or sys.argv[1:])
        self._deleted_count = 0

    def parse_args(self, args):
        parser = optparse.OptionParser("usage: %prog [options]")
        parser.set_defaults(
            hosts="g1mgos01.bs.pro.gomeplus.com:30000,"
                "g1mgos02.bs.pro.gomeplus.com:30000,"
                "g1mgos03.bs.pro.gomeplus.com:30000",
            timeout=15000,
            batch_user=100,
            batch_delete=2500,
            sleep_time=0.05)

        parser.add_option("-H", "--hosts", dest="hosts",
                            help="hosts of mongos")
        parser.add_option("-t", "--timeout", dest="timeout", type=int,
                            help="timeout to connect mongos(d), unit: ms")
        parser.add_option("-b", "--batch_user", dest="batch_user", type=int,
                            help="batch user count")
        parser.add_option("-d", "--batch_delete", dest="batch_delete", type=int,
                            help="batch delete count")
        parser.add_option("-s", "--sleep_time", dest="sleep_time", type=float,
                            help="sleep time, unit: s")
        #parser.add_option("-u", "--user", dest="user",
        #                    help="user")
        #parser.add_option("-p", "--password", dest="password",
        #                    help="passoword")
        options, _ = parser.parse_args()
        options.hosts = options.hosts.split(",")
        if options.timeout < 0:
            parser.error("invalid timout(%s < 0)" % options.timeout)
        if options.batch_user <= 0:
            parser.error("invalid batch_user(%s <= 0)" % options.batch_user)
        if options.batch_delete <= 0:
            parser.error("invalid batch_delete(%s <= 0)" % options.batch_delete)
        if options.sleep_time < 0:
            parser.error("invalid sleep_time(%s <= 0)" % options.sleep_time)
        return options

    @contextlib.contextmanager
    def make_connection(self, host=None):
        conn = pymongo.MongoClient(host=host or self.options.hosts,
                serverSelectionTimeoutMS=self.options.timeout,
                w=2)
        yield conn
        conn.close()

    def find_max_and_min(self, conn):
        # TODO: (refactor) how to gen MAX userId and MIN userId
        max, min = None, None
        for doc in conn.feed.userBatch.find({}, {"userId": 1}).sort(
            [("userId", pymongo.DESCENDING)]).limit(1):
            max = doc["userId"]
        for doc in conn.feed.userBatch.find({}, {"userId": 1}).sort(
            [("userId", pymongo.ASCENDING)]).limit(1):
            min = doc["userId"]
        return max, min

    def _delete(self, conn, idlst):
        ret = conn.feed.feedTopic.delete_many({"_id": {"$in": idlst}})
        #print "\033[31mdeleted count: %s\033[0m" % ret.deleted_count
        self._deleted_count = self._deleted_count + ret.deleted_count
        time.sleep(self.options.sleep_time)

    def batch_delete_feed(self, conn, feed_cursor):
        tmplst = []
        for doc in feed_cursor:
            tmplst.append(doc["_id"])
            if len(tmplst) >= self.options.batch_delete:
                self._delete(conn, tmplst)
                tmplst = []
        if tmplst:
            self._delete(conn, tmplst)

    def execute(self):
        __start_time = time.time()
        with self.make_connection() as conn:
            max, min = self.find_max_and_min(conn)
            while min <= max:
                next = min + self.options.batch_user
                #print "\033[32muserId: %s - %s\033[0m" % (min, next)
                user_cursor = conn.feed.userBatch.find(
                    {"userId": {"$in": range(min, next)}},
                    {"userId":1, "batchKey":1, "_id":0})
                condition = [{"userId": _doc["userId"],
                    "batchKey": {"$lt": _doc["batchKey"]}}
                    for _doc in user_cursor]
                if condition:
                    feed_cursor = conn.feed.feedTopic.find({"$or": condition},
                        {"_id":1})
                        #{"userId":1, "batchKey":1, "_id":1})
                    self.batch_delete_feed(conn, feed_cursor)
                min = next
        print "\033[32mtotal cost time: %.3fs, %s rows deleted@%s\033[0m" % (
            time.time() - __start_time, self._deleted_count, 
            time.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    Executor().execute()

