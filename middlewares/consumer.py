# -*- coding:UTF-8 -*-

import redis
from models import wechat_personal_AutoReplay, email_server

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
type = sys.getfilesystemencoding()

class Task(object):
    def __init__(self):
        self.rcon = redis.StrictRedis(host='localhost', db=5)
        self.queue = 'task:wechat:queue'

    def listen_task(self):
        while True:
            task = self.rcon.blpop(self.queue, 0)[1]
            task = eval(task)

            server_type = task.get('type')
            if server_type == 'auto_reply':
                message = task.get('text')
                user = task.get('user_id')
                # 必须一个用户扫完下一个才能继续扫。。。。
                wechat_personal_AutoReplay.auto_reply(message)
            elif server_type == 'email':
                key_s = task.get('email_key')
                from_user = task.get('from_user')
                to_user = task.get('to_user')
                text = task.get('content')
                title = task.get('title')
                email_server.email_send(title, text, to_user, from_user, key_s)





if __name__ == '__main__':
    print 'listen task queue'
    Task().listen_task()