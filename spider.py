#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 13:16:19 2021

@author: kaydee
"""

import scrapy
from scrapy.crawler import CrawlerProcess

class Sasori(scrapy.Spider):
    
    def start_requests(self):
        url = ("https://www.sololearn.com/Blog")
        yield scrapy.Request(url = url, callback = self.parse)
        
    def parse(self, response):
        pass
    
    

hiroku = CrawlerProcess()
hiroku.crawl(Sasori)
