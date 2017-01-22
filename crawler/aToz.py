#!/usr/bin/env python
# encoding: utf-8
import optparse
import string,collections

import time

L = collections.Counter(string.ascii_lowercase * 10);
print string.ascii_lowercase
print L
K = "".join([chr(i) for i in range(ord("a"),ord("z")+1)])
print K

parser = optparse.OptionParser("usage: %prog [options]")
print parser.get_default_values()

print "\033[32mtotal cost time: %.3fs, %s rows deleted@%s\033[1m" % (
    time.time() - time.time(), 123,
    time.strftime("%Y-%m-%d %H:%M:%S"))