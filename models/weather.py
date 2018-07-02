#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from lxml import etree
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
type=sys.getfilesystemencoding()
def weather_search():
    url_header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
    weather_url = 'http://www.weather.com.cn/weather/101010100.shtml'
    html = requests.get(weather_url, headers=url_header).content
    response = etree.HTML(html)
    result = response.xpath('//input[@id="hidden_title"]/@value')[0]
    return result
