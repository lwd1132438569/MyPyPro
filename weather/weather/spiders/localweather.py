# -*- coding: utf-8 -*-

import scrapy
from bs4 import BeautifulSoup
from weather.items import WeatherItem

class WeatherSpider(scrapy.Spider):
    # name = "myweather"
    # allowed_domains = ["sina.com.cn"]
    # start_urls = ['http://weather.sina.com.cn']
    #
    # def parse(self, response):
    #     item = WeatherItem()
    #     item['city'] = response.xpath('//*[@id="slider_ct_name"]/text()').extract()  #城市
    #     item['date'] = response.xpath('//*[@p.slider_ct_date]/text()').extract()      #日期
    #     item['dayDesc'] = response.xpath('//*[@p.slider_detail]/text()').extract()   #天气描述
    #     item['dayTemp'] = response.xpath('//*[@div.slider_degree]/text()').extract()   #温度
    #     # tenDay = response.xpath('//*[@id="blk_fc_c0_scroll"]');
    #     # item['date'] = tenDay.css('p.wt_fc_c0_i_date::text').extract()
    #     # item['dayDesc'] = tenDay.css('img.icons0_wt::attr(title)').extract()
    #     # item['dayTemp'] = tenDay.css('p.wt_fc_c0_i_temp::text').extract()

    name = "weather"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://weather.sina.com.cn']

    def parse(self, response):
        html_doc = response.body
        # html_doc = html_doc.decode('utf-8')
        soup = BeautifulSoup(html_doc)
        itemTemp = {}
        itemTemp['city'] = soup.find(id='slider_ct_name')
        tenDay = soup.find(id='blk_fc_c0_scroll')
        itemTemp['date'] = tenDay.findAll("p", {"class": 'wt_fc_c0_i_date'})
        # itemTemp['dayDesc'] = tenDay.findAll("img", {"class": 'icons0_wt'})
        itemTemp['dayDesc'] = tenDay.findAll("p", {"class": 'wt_fc_c0_i_tip'})
        itemTemp['dayTemp'] = tenDay.findAll('p', {"class": 'wt_fc_c0_i_temp'})
        item = WeatherItem()

        for att in itemTemp:
            item[att] = []
            if att == 'city':
                item[att] = itemTemp.get(att).text
                continue
            for obj in itemTemp.get(att):
                item[att].append(obj.text)
                # if att == 'dayDesc':
                #     item[att].append(obj['title'])
                # else:
                #     item[att].append(obj.text)

        return item