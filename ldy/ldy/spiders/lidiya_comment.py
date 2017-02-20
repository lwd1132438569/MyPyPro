# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ldy.items import LdyItem
import re

class LdySpider(scrapy.Spider):
    name = "ldy"
    allowed_domains = ["i.meituan.com"]
    start_urls = ['http://i.meituan.com/deal/27338824/feedback']

    def do_res_user(self, res):          #函数用来解析提取用户名
        res_final = []
        for it in res:
            it = str(it)
            soup = BeautifulSoup(it)
            res_mid = soup.find("weak").get_text().strip()
            res_final.append(res_mid)

        return res_final

    def do_res_comment(self, res):          #函数用来提取该情形下无属性p标签里面的内容
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

        res_us = soup.find_all("weak" , {"class": 'username'})
        mid_us = LdySpider()
        itemTemp['user'] = mid_us.do_res_user(res_us)

        res_cm = soup.find_all("div", {"class": 'toggleContent'})
        mid_cm = LdySpider()
        itemTemp['comment'] = mid_cm.do_res_comment(res_cm)

        item = LdyItem()

        for attr in itemTemp:
            item[attr] = []
            for obj in itemTemp.get(attr):
                item[attr].append(obj)

        return item