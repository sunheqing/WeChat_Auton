#coding=utf-8
import sys
import ncmbot
import json
reload(sys)
sys.setdefaultencoding('utf-8')
type=sys.getfilesystemencoding()
def WXmusic(str):
    music_json = json.loads(ncmbot.search(keyword=str).content)

    music_list_no_id=[]
    music_id=[]
    num=1
    for i in music_json['result']['songs']:
        music_list_no_id.append(u'#%s:%s--%s'%(num,i['name'],i['artists'][0]['name']))
        music_id.append(i['id'])
        num=num+1
    return music_list_no_id, music_id

def WXmusic_search(id):
    music_url_json = json.loads(ncmbot.music_url([id]).content)
    return music_url_json['data'][0]['url']


