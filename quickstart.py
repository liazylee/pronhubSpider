#!/usr/bin/env python
# coding=utf-8
__auther__ = 'liazylee'
# connect='li233111@gmail.com'
# @Time    : 6/20/19 3:37 PM
# @FileName: quickstart.py
# @Software: PyCharm
# @project: pronhubSpider


from scrapy import cmdline

cmdline.execute('scrapy crawl pronhub'.split())
