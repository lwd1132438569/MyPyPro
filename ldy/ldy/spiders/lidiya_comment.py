# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ldy.items import LdyItem
import re

class LdySpider(scrapy.Spider):
    name = "ldy"
    allowed_domains = ["i.meituan.com"]
    start_urls = ['http://i.meituan.com/deal/27338824.html?stid=831871120134148096_b0_e7503411704774631424_a%E8%8E%89%E8%BF%AA%E4%BA%9A_f1491862']

    def do_res(self, res):          #函数用来提取该情形下无属性p标签里面的内容
        res_final = []
        for it in res:
            it = str(it)
            soup = BeautifulSoup(it)
            res_mid = soup.find("p").get_text().strip()
            res_final.append(res_mid)

        return res_final


    def parse(self, response):
        html_doc = response.body
        soup = BeautifulSoup(html_doc)
        itemTemp = {}
        # itemTemp['user'] = soup.find_all("span",{"class":'name vip_level_high'})
        res_div = soup.find_all("div", {"class": 'toggleContent'})

        mid = LdySpider()
        itemTemp['comment'] = mid.do_res(res_div)

        item = LdyItem()

        for attr in itemTemp:
            item[attr] = []
            for obj in itemTemp.get(attr):
                item[attr].append(obj)

        return item