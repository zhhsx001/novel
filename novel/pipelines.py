# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class NovelPipeline(object):
    def process_item(self, item, spider):
        if not os.path.exists('/home/zhanghua/fantasy_novels/%s/' % (item['novel'])):
            os.makedirs('/home/zhanghua/fantasy_novels/%s/' % (item['novel']), exist_ok=True)
        filename = '/home/zhanghua/fantasy_novels/%s/%s.txt' % (item['novel'], item['chapter'])
        with open(filename, 'w') as f:
            f.write(item['content'])
        return item