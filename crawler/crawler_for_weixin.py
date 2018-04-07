#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import urllib
import re
import os
import traceback
import requests
import json
from lxml import etree



def http_get(url,timeout=None):
    header={
    
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
    req=urllib2.Request(url,headers=header)
    if timeout:
        result= urllib2.urlopen(req,timeout).read()
    else:
        result= urllib2.urlopen(req).read()
    return result
    
    
global count
count=0
def parse_weixin(html):

    dom_tree = etree.HTML(html)
    
    prefix= 'https://mp.weixin.qq.com'
    

            
        s=str('name: '+title+' url: '+str(href) )
        
        print s

    
def main():

    url='https://mp.weixin.qq.com/profile?src=3&timestamp=1522931819&ver=1&signature=SfnF0ktqWCx5Ym7IaoXKRvbPcllyHkVXuAUOlQWtgCzCNAbbpxW2Rx*NX-r1E3MGxjU9JYLhoQxs5VajIya0aQ=='
    print 'begin downloading!'
    html=http_get(url)
    
    print 'download finished!'

    print 'begin parsing static html'
    
    parse_weixin(html)


if __name__ == '__main__':
    print '开始'.decode('utf-8')
    main()
