#coding=utf-8
from __future__ import division  #实数化除法
import time
t1=time.time()
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
type = sys.getfilesystemencoding()
def deal_field(ustring):   #这里要用Unicode编码
    for ch in ustring:
        if (u'\u4e00' <= ch and ch <= u'\u9fff') or (u'\u0041'<=ch and ch<=u'\u005A') or (u'\u0061'<=ch and ch<=u'\u007A'):
            pass
        else:
            ustring = ustring.replace(ch, '')
    return ustring
def levenshtein(str_1,str_2):   #这里要用utf-8编码
    len_1 = len(str_1)
    len_2 = len(str_2)
    dp_list = []

    for i in range(0, len_1 + 1):
        dp_list.append([])
        dp_list[i].append(i)

    for i in range(1, len_2 + 1):
        dp_list[0].append(i)

    for i in range(1, len_1 + 1):
        for j in range(1, len_2 + 1):
            if str_1[i - 1] == str_2[j - 1]:
                dp_list[i].append(dp_list[i - 1][j - 1])
            else:
                dp_mark = min(dp_list[i - 1][j - 1], min(dp_list[i][j - 1], dp_list[i - 1][j])) + 1
                dp_list[i].append(dp_mark)

    return 1-dp_list[len_1][len_2]/max(len_2,len_1)

def similar_music(code_str):
    new = deal_field(code_str.decode('utf-8')).encode('utf-8')
    word_list = ['听歌', '音乐', 'yinyue', 'music', 'song', '歌曲']
    for i in word_list:
        if levenshtein(new,i)>=0.5:
            return True
    return False

def similar_weather(code_str):
    new = deal_field(code_str.decode('utf-8')).encode('utf-8')
    word_list = ['天气', 'weather', '气候']
    for i in word_list:
        if levenshtein(new,i)>=0.5:
            return True
    return False

def similar_email(code_str):
    new = deal_field(code_str.decode('utf-8')).encode('utf-8')
    word_list = ['邮件', 'email', '电子邮件']
    for i in word_list:
        if levenshtein(new,i)>=0.5:
            return True
    return False

def similar_news(code_str):
    new = deal_field(code_str.decode('utf-8')).encode('utf-8')
    word_list = ['新闻', 'xinwen', 'news', '资讯', 'zixun', '头条', 'toutiao']
    for i in word_list:
        if levenshtein(new,i)>=0.5:
            return True
    return False

def similar_movie(code_str):    #xml信息流是utf-8编码
    new = deal_field(code_str.decode('utf-8')).encode('utf-8')
    word_list = ['电影', 'dianying', 'movie', '票房', 'piaofang', '影片', 'yingpian']
    for i in word_list:
        if levenshtein(new,i)>=0.5:
            return True
    return False

def similar_wxRobot(code_str):    #xml信息流是utf-8编码
    new = deal_field(code_str.decode('utf-8')).encode('utf-8')
    word_list = ['微信机器人', '微信个人号', '微信代理', 'wxrobot', 'wechatrobot', '机器人', 'robot']
    for i in word_list:
        if levenshtein(new,i)>=0.6:
            return True
    return False

