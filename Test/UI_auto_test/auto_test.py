#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import random
c_path = os.path.abspath(r"D:\chromedriver\chromedriver.exe")  #PhantomJS凉了

browser = webdriver.Chrome(c_path)
browser.get('http://127.0.0.1:5000/login')
browser.maximize_window()
time.sleep(3)
browser.find_element_by_xpath('//input[@type="text"]').send_keys(u"田旭")
time.sleep(2)
browser.find_element_by_xpath('//*[@type="reset"]').click()
time.sleep(2)
browser.find_element_by_xpath('//input[@type="text"]').send_keys(u"孙合庆")
browser.find_element_by_xpath('//*[@type="submit"]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="in"]').send_keys(u"天气查询代码")
time.sleep(2)
browser.find_element_by_xpath('//*[@id="in"]').send_keys(Keys.ENTER)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="in"]').send_keys(u"新闻查询代码")
time.sleep(2)
browser.find_element_by_xpath('//*[@id="in"]').send_keys(Keys.ENTER)
browser.find_element_by_xpath('//a[@href="/logout"]').click()