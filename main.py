# -*- coding: utf-8 -*-
# filename: main.py
import web
import os
from handle import Handle,News,Email

urls = (
    '/', 'Handle',
    '/news/(.*)', 'News',
    #'/email', 'Email',
    #'/help', 'Help',

)
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
