# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from lidiya.items import LidiyaItem
import re

class LidiyaSpider(scrapy.Spider):
    name = "lidiya"
    allowed_domains = ["jn.meituan.com"]
    start_urls = ['http://jn.meituan.com/shop/1491862?acm=UmyulwbVm_16524168776346421733.%E8%8E%89%E8%BF%AA%E4%BA%9A%E6%84%8F%E5%BC%8F%E4%BC%91%E9%97%B2%E9%A4%90%E5%8E%85.1W593132266326748274.27338824.9.27338824.1&mtt=1.deal%2Fdefault.0.0.iz9334ln&cks=10744']

    def parse(self, response):
        html_doc = response.body
        soup = BeautifulSoup(html_doc)
        itemTemp = {}
        itemTemp['user'] = soup.find_all("span",{"class":'name vip_level_high'})
        itemTemp['comment'] = soup.find_all("p",{"class":'content'})
        item = LidiyaItem()

        for attr in itemTemp:
            item[attr] = []
            for obj in itemTemp.get(attr):
                item[attr].append(obj.text)

        return item