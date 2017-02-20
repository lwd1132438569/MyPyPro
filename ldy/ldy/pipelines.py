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
            user = item['user']
            comment = item['comment']
            # for i in range(len(comment)):
            #     file.write(comment[i].encode('utf-8'))

            ldyitem = zip(user,comment)

            for i in range(len(ldyitem)):
                item = ldyitem[i]
                us = item[0]
                cm = item[1]
                txt = '用户：{0}\t的评论：{1}\n'.format(
                    us.encode('utf-8'),
                    cm.encode('utf-8')
                )
                file.write(txt)

        return item
