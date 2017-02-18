# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LdyPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        with open('ldy.txt', 'w+') as file:

            comment = item['comment']

            ldyitem = zip(comment)

            for i in range(len(ldyitem)):
                cm = ldyitem[0]
                txt = '评论:{0}\t'.format(
                    cm.encode('utf-8')
                )
                file.write(txt)
