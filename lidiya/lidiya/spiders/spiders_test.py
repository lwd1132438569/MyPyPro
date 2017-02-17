# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib2

# def getHtml(url):
#     headers = ('User-Agent',
#     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
#     opener = urllib.request.build_opener()
#     opener.addheaders = [headers]
#     htmldata = opener.open(url).read()
#     htmldata=htmldata.decode('utf-8')
#     return htmldata

url = 'http://jn.meituan.com/shop/1491862?acm=UmyulwbVm_16524168776346421733.%E8%8E%89%E8%BF%AA%E4%BA%9A%E6%84%8F%E5%BC%8F%E4%BC%91%E9%97%B2%E9%A4%90%E5%8E%85.1W593132266326748274.27338824.9.27338824.1&mtt=1.deal%2Fdefault.0.0.iz9334ln&cks=10744'
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
conn = urllib2.urlopen(url,timeout=5)
html = conn.read()
soup = BeautifulSoup(html)

res = soup.find_all("p",{"class":'content'})
print res

