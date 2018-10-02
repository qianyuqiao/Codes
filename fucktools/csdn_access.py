# -*- coding: utf-8 -*-

# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/7/17'
# 邮箱：fonttian@Gmaill.com
# CSDN：http://blog.csdn.net/fontthrone
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import socket
import time
import re
import random

# 在这里填写你要访问的博客地址
blog_url = [
    'http://blog.csdn.net/fontthrone/article/details/75212825',
    'http://blog.csdn.net/FontThrone/article/details/75136885',
    'http://blog.csdn.net/FontThrone/article/details/75042659',
    'http://blog.csdn.net/FontThrone/article/details/74230603',
    'http://blog.csdn.net/FontThrone/article/details/74201764',
]


class CSDN(object):
    def __init__(self, blog_url=blog_url, csdn_url="http://blog.csdn.net/fontthrone"):
        self.blog_url = blog_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip',
            'Connection': 'close',
            'Referer': None
        }

    def openCsdn(self):
        req = urllib2.Request(self.csdn_url, headers=self.headers)
        response = urllib2.urlopen(req)
        thePage = response.read()
        response.close()
        pattern = "访问：<span>(\d+)次</span>"
        number = ''.join(re.findall(pattern, thePage))
        return number

    def openBlog(self, link='http://blog.csdn.net/fontthrone/article/details/70556507', timeout=60, sleepTime=22,
                 maxTryNum=1):
        tries = 0
        maxNum = 0
        # for tries in range(maxTryNum):
        while tries < maxTryNum:
            try:
                socket.setdefaulttimeout()
                req = urllib2.Request(link, None, self.headers)
                resp = urllib2.urlopen(req, None, timeout)
                html = resp.read()
                print "Success!\t",
                print "Rest ", sleepTime, " seconds to continue...\n"
                tries += 1
                time.sleep(sleepTime)
            except:
                if tries < (maxTryNum):
                    maxNum += 1
                    continue
                else:
                    print("Has tried %d times to access blog link %s, all failed!", maxNum, link)
                    break

    def start(self, maxTime=100, blOpenCsdn=False, sleepTimeStart=5, sleepTimeEnd=15, timeout=60):
        for i in range(maxTime * len(self.blog_url)):
            randomLink = random.choice(self.blog_url)
            print 'This tinme the random_blog link is ', randomLink
            if blOpenCsdn == True:
                self.openCsdn()
            self.openBlog(link=randomLink, sleepTime=random.uniform(sleepTimeStart, sleepTimeEnd), timeout=timeout)
            print "Now is " + str(i + 1) + " times to acess blog link\n"


csdn = CSDN()
inputMaxTime = input(u'请输入列表访问次数\n')
csdn.start(maxTime=int(inputMaxTime))