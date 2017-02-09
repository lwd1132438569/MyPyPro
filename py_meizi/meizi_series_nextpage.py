#-*- coding: utf-8 -*-

import re
import urllib2
#这个呢，是获取组图套图的代码，是下一个需要显示的代码块
import meizi_series_getpage
#同样的，这里是加载链接防超时，和上一节一样

def loadurl(url):
    try:
        conn = urllib2.urlopen(url, timeout=5)
        html = conn.read()
        return html
    except urllib2.URLError:
        return ""
    except Exception:
        print("unkown exception in conn.read()")
        return ""

def nextpage(url,path):
    reNextLink = "<a.*?href='(.*?)'>.*?</a>"
    #获取reNextPage里的标签的全部链接
    reNextPage = '<div.*?id="wp_page_number.*?>.*?<ul>(.*?)</ul>'
    #获取ul标签里面的内容，里面包含了所有我们需要的链接，找到wp_page_number就可以了
    #下面目的是获取链接名，组合传入路径得到当前路径名，解释：匹配a到z字符，>=1个
    searchPathTail = '.*/([a-z]+).*?.html'
    #获取传入的链接尾巴
    searchurltail = '.*/(.*?.html)'
    #获取传入的链接头部
    searchhead = '(.*)/.*?.html'

    # 分开头和尾，是因为在获取当前标签的所有页码，都不是完整的，而是尾部链接，需要用尾部和头部链接拼凑成完整的链接。头部链接，就是传入链接的头部，而且传入的是第一个完整链接，页面1里面又没有尾部链接，所有传入链接的尾部，也需要找出
    pathTail = re.findall(searchPathTail, url, re.S)
    urlTail = re.findall(searchurltail, url, re.S)
    urlhead = re.findall(searchhead, url, re.S)
    # 从传入文件夹路径和从链接中分析出的文件名，得到当前文件夹路径，保存到path中
    path = path + '/' + pathTail[0]
    print path

    # 标签页面的存储列表nextpage
    nextpageurl = []
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            print 'load', url, 'error'
            continue
        else:
            break
    nextPage = re.findall(reNextPage, html, re.S)
    nextLink = re.findall(reNextLink, nextPage[0], re.S)
    nextLink.append(urlTail[0])

    # 这一段是将标签页码的所有尾部链接保存到nextLink中，然后下面的for循环，将完整的url链接，存储到nextpageurl中
    nextLink = sorted(list(set(nextLink)))
    for i in nextLink:
        nextpageurl.append(urlhead[0] + "/" + i)
    # 将url链接和对应的文件路径传入"获取标签第n页的所有组图链接"的模板中，引号标记的，就是下一个代码块
    for i in nextpageurl:
        print i
        meizi_series_getpage.tag_series(i, path)



