#coding=utf-8
import redis
import pymysql

#连接MySQL
db = pymysql.connect(host="localhost", user="root", password="123456", db="website", port=3306, charset='utf8')

#连接Redis
redis_db = redis.Redis(host='127.0.0.1', port=6379,db=0)
redis_db_2 = redis.StrictRedis(host='localhost', db=5)
#redis_db.set('oHfuz0hYUIrqM6b410E7nK8TnlGE', 'other_serving')
#redis_db.set('about_text', '暂无')
#print redis_db.get('sunkey')
#redis_db.set('sunkey','ed')
#print redis_db.get('sunkey')
#music_list = [2,2,2,2]
#for i in eval(redis_db.get('sunkey_content')):
#    print i
