# -*- coding: utf-8 -*-
import os
import pandas as pd
import scrapy
from bs4 import BeautifulSoup
from novel.items import NovelItem


class AllNovelSpider(scrapy.Spider):
    name = 'all_novel'
    allowed_domains = ['www.xbiquge.la']
    start_urls = ['http://www.xbiquge.la/xiaoshuodaquan/']

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        novels = soup.find(id='main').find_all(name='a')
        for novel in novels:
            novel_url = novel.get('href')
            novel_name = novel.text
            yield scrapy.Request(url=novel_url, meta={'novel': novel_name, 'novel_url': novel_url}, callback=self.table)

    def table(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        table = soup.find(id='list').find_all(name='dd')
        for chapter in table:
            item = NovelItem()
            item['novel'] = response.meta['novel']
            item['novel_url'] = response.meta['novel_url']
            chapter_url = 'http://www.xbiquge.la/' + chapter.a.get('href')
            item['chapter'] = chapter.text
            item['chapter_url'] = chapter_url
            yield scrapy.Request(url=chapter_url, meta={'item': item}, callback=self.content)

    def content(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.body, 'lxml')
        content = soup.find(id='content')
        p = content.find(name='p')
        p.extract()
        item['content'] = content.text
        yield item
