#!/usr/bin/env python
# coding=utf-8
import logging
import re

from scrapy import Request, Selector
from scrapy_splash import SplashRequest

from pronhubSpider import settings
from pronhubSpider.items import PronhubspiderItem

__auther__ = 'liazylee'
# connect='li233111@gmail.com'
# @Time    : 6/20/19 3:29 PM
# @FileName: pronhub.py
# @Software: PyCharm
# @project: pronhubSpider

from scrapy.spiders import CrawlSpider

script = """
function main(splash, args)
  splash:autoload([[
    function get_video(){
    
      return flashvars;
    }
  ]])
  assert(splash:go(args.url))
  return {
            q480=splash:evaljs("get_video()"),
             
        }
end
"""


class Pronhub(CrawlSpider):
    name = 'pronhub'

    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='tail_log.log',
                        filemode='w')

    def start_requests(self):
        for ph_type in settings.PHTYPE:
            yield SplashRequest(url='https://www.pornhub.com/{}'.format(ph_type), callback=self.parse,args={'wait':1})

    def parse(self, response):
        selector = Selector(response)
        logging.debug('request url  ---->' + response.url)
        response_selectors = selector.xpath('//div[@class="phimage"]')
        for response_selector in response_selectors:
            view_key = re.findall('viewkey=(.*?)"', response_selector.extract())
            yield SplashRequest(url='https://www.pornhub.com/embed/{}'.format(view_key[0]),
                                callback=self.parse_key,
                                endpoint='execute',
                                args={'lua_source': script})
        # selector_next_url=response.css('head > link:nth-child(42)')
        next_url = selector.xpath('//a[@class="orangeButton" and text()="Next "]/@href').extract_first()
        logging.debug('next_url:----->' + str(next_url))
        if next_url:
            yield SplashRequest(url='https://www.pornhub.com{}'.format(next_url), callback=self.parse,args={'wait':1})
        pass

    def parse_key(self, response):
        phItem = PronhubspiderItem()
        selector = response.data['q480']
        # logging.info(selector)
        # _ph_info = re.findall('var flashvars =(.*?),\n', selector)
        # logging.debug('PH信息的JSON:')
        # logging.debug(_ph_info)
        # _ph_info_json = json.loads(_ph_info[0])
        duration = selector.get('video_duration')
        phItem['video_duration'] = duration
        title = selector.get('video_title')
        phItem['video_title'] = title
        image_url = selector.get('image_url')
        phItem['image_url'] = image_url
        link_url = selector.get('link_url')
        phItem['link_url'] = link_url
        quality_480p = selector.get('mediaDefinitions')[0].get('videoUrl')
        # quality_480p = _ph_info_json.get('quality_480p')
        phItem['quality_480p'] = quality_480p
        # logging.info('duration:' + duration + ' title:' + title + ' image_url:'
        #              + image_url + ' link_url:' + link_url,'quality_480p:'+quality_480p)
        # pprint.pprint(phItem)
        yield phItem

