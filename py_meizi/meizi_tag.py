#-*- coding: utf-8 -*-

import re
import urllib2
import meizi_series_nextpage

def loadurl(url):
    try:
        conn = urllib2.urlopen(url,data=None,timeout=5)
        html = conn.read()
        return html
    except Exception:
        return ''

def meizi(url,path):
    #见上面的html代码截图，对比无误
    reTagContent = '<div.*?class="tags">.*?<span>(.*?)</span>'
    reTagUrl = '<a.*?href="(.*?)".*?>'
    print 'start open meiziwang'
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            print 'load', url,'error'
            continue
        else:
            break

    tagContent = re.findall(reTagContent, html, re.S)
    taglists = re.findall(reTagUrl, tagContent[0], re.S)
    # 你仔细看会发现，链接又重，而且匹配、添加到列表，重复依旧在，所以啦，需要去重和排序，
    taglists = sorted(list(set(taglists)))
    for url in taglists:
        meizi_series_nextpage.nextpage(url, path)


meizi('http://www.meizitu.com', '/home/shiyanlou/Desktop/meizi')
print 'Spider Stop'