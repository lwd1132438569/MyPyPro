#-*- coding: utf-8 -*-

import re
import urllib2
import meizi_page_download

def loadurl(url):
    #依旧的，防超时和循环加载
    try:
        conn = urllib2.urlopen(url,timeout=5)
        html = conn.read()
        return html
    except urllib2.URLError:
        return ''
    except Exception:
        print("unkown exception in conn.read()")
        return ''

#这个函数，简单点就是根据套图链接和传入的路径，得到套图文件夹路径，再传给上一节的图片下载模板

def oneOfSeries(urllist,path):
    searchname = '.*/(.*?).html'
    current_path = ''
    for url in urllist:
        try:
            name = re.findall(searchname,url,re.S)
            current_path = path + '/' + name[0]
            meizi_page_download.picurl(url,current_path)
        except urllib2.URLError:
            pass

#传入标签的第n页和文件夹路径，获取所有套图url链接，和分析出对应的文件夹路径，传给我们底层的图片下载模板（也就是上一节啦）

def tag_series(url,path):
    #这里是直接匹配出套图的链接，直接，注意是直接，最好是将结果和源码对下结果，防止遗漏和多出
    reSeriesList = '<div .*?class="pic".*?>.*?<a.*?href="(.*?)".*?target.*?>'
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            print 'load', url,'error'
            continue
        else:
            break
    seriesList = re.findall(reSeriesList,html,re.S)
    if len(seriesList) == 0:
        pass
    else:
        oneOfSeries(seriesList, path)