#-*- coding: utf-8 -*-

import urllib2
import os
import re

#loadurl()这个函数呢，是防打开链接超时，如果超时返回空字符，则主调函数会再次调用(while语句就可以实现)，正常的话返回html代码，一个网页不算大，如果你的网络超级好，timeout可以缩短
def loadurl(url):
    try:
        conn = urllib2.urlopen(url,timeout=5)
        html = conn.read()
        return html
    except urllib2.URLError:
        return ''
    except Exception:
        print("unkown exception in conn.read()")
        return ''

#这里是图片保存的代码被调函数，timeout=5设置超时时间，一个500k不到的图片，5秒时间算长的了，超时的话，返回失败

def download(url,filename):
    try:
        conn = urllib2.urlopen(url,timeout=5)
        f = open(filename,'wb')
        f.write(conn.read())
        f.close()
        return True
    except urllib2.URLError:
        print 'load',url,'error'
        return False
    except Exception:
        print("unkown exception in conn.read()")
        return ''

#保存图片的逻辑代码块
def save_pic(url,path):
    searchname = '.*/(.*?.jpg)'
    name = re.findall(searchname,url)
    filename = path +'/'+ name[0]

    print filename + ':start' #控制台显示信息

    #下面的代码，当下载成功，break跳出就好了，如果存在，直接结束这个函数

    #定义了在下载图片时遇到错误的重试次数
    tryTimes = 3

        #当重试次数没有用完时，则尝试下载


    while tryTimes != 0:
        tryTimes -= 1
        if os.path.exists(filename):
            print filename, ' exists, skip'
            return True
        else:
            os.makedirs(filename)
        if download(url, filename):
            break

    if tryTimes != 0:
        print(filename + ": over")
    else:
        print(url + " ：Failed to download")
        # 控制台显示信息

#这个函数，相当于一个中介，我只是把for循环代码提出就得到了这个函数
def pic_list(picList,path):
    picurl = ''
    for picurl in picList:
        save_pic(picurl,path)

#图片下载的主逻辑函数，获取图片链接，然后传给pic_list()，等结果(其实也没结果，就是等退出)
def picurl(url,path):
    if os.path.exists(path):
        print path, 'exist'
    else:
        os.makedirs(path)
    html = ''
    while True:#这里和下载图片是一个道理，细看即可
        html = loadurl(url)
        if html == '':
            print 'load', url,'error'
            continue
        else:
            break

#其实这里呢，也是后期发现的一个小bug，这个网站的前后代码有不同（目前而言发现的一处），在rePicContent1运行到后面，是匹配不到的，导致rePicList返回的结果也是空，也就造成了这个符号[0]报错，因为没有任何值，越界错误,单线程会在这里报错并停止运行。rePicContent2其实是我解决bug的另一个匹配正则式，被我发现的页面是这个--http://www.meizitu.com/a/454.html，有兴趣的去对比看看
    rePicContent1 = '<div.*?id="picture.*?>.*?<p>(.*?)</p>'
    rePicContent2 = '<div.*?class="postContent.*?>.*?<p>(.*?)</p>'
    rePicList = '<img.*?src="(.*?)".*?>'

#这里对re.S做个介绍，re.S是可以不添加的，加上之后，它的作用就是能忽略换行符，将两条作为一条来匹配。html代码碰上换行的概率是很高的，所以我一致采用re.S(下文有配图)
    picContent = re.findall(rePicContent1, html,re.S)
    if len(picContent) <=0:
        picContent = re.findall(rePicContent2, html,re.S)
    if len(picContent) <=0:
        print 'load false, over download this page and return'
        return False
    else:
        picList = re.findall(rePicList,picContent[0],re.S)
        pic_list(picList,path)

url = 'http://www.meizitu.com/a/454.html'
picurl(url,'/home/shiyanlou/Desktop/demo454')