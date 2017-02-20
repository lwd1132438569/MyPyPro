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

def do_res(res):
    res_final = []
    for it in res:
        it = str(it)
        soup = BeautifulSoup(it)
        res_mid = soup.find("p").get_text().strip()
        res_final.append(res_mid)

    return res_final

def do_res_user(res):
    res_final = []
    for it in res:
        it = str(it)
        soup = BeautifulSoup(it)
        res_mid = soup.find("weak").get_text().strip()
        res_final.append(res_mid)

    return res_final

url = "http://i.meituan.com/deal/27338824/feedback"
# headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
#     opener = urllib.request.build_opener()
#     opener.addheaders = [headers]
conn = urllib2.urlopen(url,timeout=5)
html = conn.read()
soup = BeautifulSoup(html,'lxml')
# res_div = soup.find_all("div",{"class":'toggleContent'})
# res = do_res(res_div)
# <weak class="username">小姑娘iii</weak>
res_div = soup.find_all("weak",{"class":'username'})
res = do_res_user(res_div)

print res



