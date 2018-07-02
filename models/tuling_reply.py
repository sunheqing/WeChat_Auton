#coding=utf-8
import requests
def tuling_reply(info):
    apiurl='http://www.tuling123.com/openapi/api'
    data={
        'key':'56f17053090a4a04ae1d5318557aa402',
        'info':info,
        'userid':'from_auton'
    }
    message = requests.post(url=apiurl,data=data).json()
    return message['text']
