#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ConfigParser

def config_to_dict(config_file):
    """

    :rtype: object
    """
    cf = ConfigParser.ConfigParser()
    cf.read(config_file)
    result = {}
    for section in cf.sections():
        result[section] = dict(cf.items(section))
    print result
if __name__ =='__main__':
    config_to_dict('parser.txt')

