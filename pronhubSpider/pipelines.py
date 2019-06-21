# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo as pymongo
import scrapy
from pymongo import IndexModel
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline

from pronhubSpider.items import PronhubspiderItem


class OwnFilePipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        url=request.url
        path=url.split('?')[0].split(':')[1].replace('/','')
        return path
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['quality_480p'])

    def item_completed(self, results, item, info):
        video_paths = [x['path'] for ok, x in results if ok]
        if not video_paths:
            raise DropItem('Item fail')
        item['quality_480p']=video_paths
        return item


class PronhubspiderPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("127.0.0.1", 27017)
        db = clinet["PornHub"]
        self.PhRes = db["PhRes"]
        idx = IndexModel([('link_url', pymongo.ASCENDING)], unique=True)
        self.PhRes.create_indexes([idx])
        # if your existing DB has duplicate records, refer to:
        # https://stackoverflow.com/questions/35707496/remove-duplicate-in-mongodb/35711737

    def process_item(self, item, spider):
        # print 'MongoDBItem'
        """ 判断类型 存入MongoDB """
        if isinstance(item, PronhubspiderItem):
            # print 'PornVideoItem True'
            try:
                self.PhRes.update_one({'link_url': item['link_url']}, {'$set': dict(item)}, upsert=True)
            except Exception as e:
                print(e)
        return item
