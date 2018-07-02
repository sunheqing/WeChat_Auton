# coding=utf-8
from wxpy import *


def auto_reply(message):
    bot = Bot()

    # 机器人账号自身
    # user = bot.self

    # 向文件传输助手发送消息
    bot.file_helper.send(message)
