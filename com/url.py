__author__ = 'renfei'

import urllib2
import sys

def urlTest():
    req = urllib2.Request('http://t.hd.xiaomi.com/s/?_a=20131022_phone_df56ab516d&_op=choose')
    try:
        response = urllib2.urlopen(req)
        print response.geturl()
    except urllib2.HTTPError,e:
        print e.code

urlTest()