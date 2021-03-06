# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import base64

from fake_useragent import UserAgent
from scrapy.conf import settings


class RandomUserAgent(object):

    def process_request(self, request, spider):
        useragent = UserAgent(verify_ssl=False)
        request.headers.setdefault('User-Agent', useragent)


class RandomProxy(object):

    def process_request(self, request, spider):
        proxy = random.choice(settings['PROXIES'])
        if len(proxy['user_password']) == 0:
            request.meta['proxy'] = "http://" + proxy['ip_port']
        else:
            base64_userpassword = base64.b64encode(proxy['user_password'])
            request.meta['proxy'] = "http://" + proxy['ip_port']
            request.headers['Proxy-Authorization'] = 'Basic' + base64_userpassword
