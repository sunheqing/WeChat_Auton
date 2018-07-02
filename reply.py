# -*- coding: utf-8 -*-
#  filename: reply.py
import time
from templates_xml import reply_xml

class Msg(object):
    def send(self):
        return "success"
class TextMsg(Msg):
    def __init__(self,toUserName,fromUserName,content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content
    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)

class TextUrlMsg_news(Msg):
    def __init__(self,toUserName,fromUserName,content,picurl,url):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content
        self.__dict['PicUrl'] = picurl
        self.__dict['Url'] = url
    def send(self):
        XmlForm = reply_xml.XmlForm_news
        return XmlForm.format(**self.__dict)

class TextUrlMsg_help(Msg):
    def __init__(self,toUserName,fromUserName,content,picurl,url):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content
        self.__dict['PicUrl'] = picurl
        self.__dict['Url'] = url
    def send(self):
        XmlForm = reply_xml.XmlForm_help
        return XmlForm.format(**self.__dict)


class TextUrlMsg_music(Msg):
    def __init__(self,toUserName,fromUserName,url):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Url'] = url
    def send(self):
        XmlForm = reply_xml.XmlForm_music
        return XmlForm.format(**self.__dict)

class TextUrlMsg_email(Msg):
    def __init__(self,toUserName,fromUserName,content,picurl,url):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content
        self.__dict['PicUrl'] = picurl
        self.__dict['Url'] = url
    def send(self):
        XmlForm = reply_xml.XmlForm_email
        return XmlForm.format(**self.__dict)