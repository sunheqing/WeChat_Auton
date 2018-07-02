#coding=utf-8
from flask import Flask,render_template,url_for
from flask_moment import Moment
from models import weather,movie_Finance
import time
import flask
import datetime
import redis
import sys
reload(sys)
sys.setdefaultencoding('utf8')

app=Flask(__name__)
moment = Moment(app)
app.secret_key='lovered'

#redis数据库
r=redis.StrictRedis(host='localhost',port=6379,db=1,decode_responses=True)


def event_stream():
    pubsub=r.pubsub()
    pubsub.subscribe('chat')
    for message in pubsub.listen():
        print u"控制台监控："
        print (message)
        yield 'data:{}\n\n'.format(message['data'])


#首页
@app.route('/')
def index():
    if 'user' not in flask.session:
        return flask.redirect('/login')
    user=flask.session['user']
    return render_template('index.html',user=user)

#登录页面
@app.route('/login',methods=['GET','POST'])
def login():
    if 'user' in flask.session:
        return flask.redirect('/')
    if flask.request.method=='POST':
        flask.session['user']=flask.request.form['user']
        r.publish('chat', '用户{}加入了房间!'.format(flask.session['user']))
        return flask.redirect('/')
    return render_template('login.html')

#注销
@app.route('/logout')
def logout():
    user=flask.session.pop('user')
    print(user)
    r.publish('chat', '用户{}退出了房间'.format(user))
    return flask.redirect('/login')

#发送消息
@app.route('/send',methods=['POST'])
def post():
    message=flask.request.form['message']
    time_start_w = time.time()
    if message==u"天气查询代码":
        test_text = weather.weather_search()
    #elif message==u"新闻查询代码":
     #   test_text = news.sport()
    elif message==u'电影':
        test_text = movie_Finance.movie()
    else:
        test_text = message
    time_end_w = time.time()
    time_w = u"响应时间："+str(time_end_w-time_start_w)+u"秒"
    user=flask.session.get('user','anonymous')
    now=datetime.datetime.now().replace(microsecond=0).time()
    r.publish('chat','[{}] {} : {}'.format(now.isoformat(),user,message))
    r.publish('chat', '[{}] {} : {}'.format(now.isoformat(), u"服务模块", test_text))
    r.publish('chat', '{}'.format(time_w))


    return flask.Response(status=204)

#SSE事件流
@app.route('/stream')
def stream():
    return flask.Response(event_stream(),mimetype='text/event-stream')



if __name__ == '__main__':
    app.run(debug=True, threaded=True)