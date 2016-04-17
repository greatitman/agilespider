import os
import re
#coding : utf-8
from agilespider import *

def getTitle(html):
    title = re.search('<title>(.*?)</title>',html, re.S).group(1)
    return title

if __name__=='__main__':
    html = AgileSpider.getWebPage("http://www.baidu.com")
    print getTitle(html)