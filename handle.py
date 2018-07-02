# -*- coding: utf-8 -*-
# filename: handle.py

# import hashlib
import time
from models import weather, netease_music, tuling_reply, movie_Finance
from static import norm_text
import reply
import receive
import web
from web import database, template
from settings import db, redis_db, redis_db_2
from middlewares import Levenshtein

cursor = db.cursor()


def sql(sql_talk):
    try:
        row = cursor.execute(sql_talk)
        db.commit()
    except:
        db.rollback()


import sys

reload(sys)
sys.setdefaultencoding('utf-8')
type = sys.getfilesystemencoding()

db = database(dbn='mysql', db='website', user='root', pw='123456')
render = template.render('templates')

'''
class Help:
    def GET(self):
        return render.help()
'''
class News:
    def GET(self, id):
        print id
        all_news = db.select('news', order='id DESC')
        return render.index(all_news)
        # return u'访问深度边缘的用户ID是：'+id


class Email:
    def GET(self):
        return render.email()


class Handle(object):
    def __init__(self):
        self.prodcons_queue = 'task:wechat:queue'
        self.rcon = redis_db_2

    def POST(self):

        try:
            webData = web.data()
            print u"XML信息", webData
            # 后台打日志
            recMsg = receive.parse_xml(webData)
            # 关注、取关类消息
            if isinstance(recMsg, receive.EventMsg) and recMsg.MsgType == 'event':
                to_User = recMsg.FromUserName
                from_User = recMsg.ToUserName
                user_event = recMsg.Event
                if user_event == "subscribe":
                    # print u"用户已经关注，存储进入Redis数据库"
                    '''
                    redis_db.set(to_User + '-music_server', 'sleeping')
                    redis_db.set(to_User + '-finance_server', 'sleeping')
                    redis_db.set(to_User + '-movie_server', 'sleeping')
                    redis_db.set(to_User + '-card_game_server', 'sleeping')
                    redis_db.set(to_User + '-other_server', 'serving')
                    '''
                    redis_db.set(to_User, 'other_serving')
                    return_content = r'''
    感谢您的关注！【奥谭】是一个自动应答机器人，整个项目是由本公众号、小程序【MissPaprika】以及微信个人号组成

    首次使用？输入#help获取帮助文档
    了解更多？输入#about了解项目进展，联系开发者！
                    ''' + '\n' + norm_text.hi_text
                    replyMsg = reply.TextMsg(to_User, from_User, return_content)
                    return replyMsg.send()
            # 文本消息
            elif isinstance(recMsg, receive.TextMsg) and recMsg.MsgType == 'text':

                to_User = recMsg.FromUserName
                from_User = recMsg.ToUserName
                time = recMsg.CreateTime
                user_content = recMsg.Content
                if user_content == '#help':
                    return_content = u'Hand Book'
                    url = 'https://mp.weixin.qq.com/s/ofbuqlerprJDOQ7t9Hh-_g'
                    picurl = r'https://img3.doubanio.com/view/photo/l/public/p2521569791.webp'
                    replyMsg = reply.TextUrlMsg_help(to_User, from_User, return_content, picurl, url)
                    return replyMsg.send()

                if redis_db.get(to_User) == 'other_serving':

                    if Levenshtein.similar_weather(user_content) == True:
                        return_content = weather.weather_search()
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif Levenshtein.similar_news(user_content) == True:
                        # print to_User
                        return_content = u'深度边缘'
                        url = 'http://shq.s1.natapp.cc/news/' + to_User
                        picurl = r'https://img3.doubanio.com/view/photo/l/public/p2383768230.webp'
                        replyMsg = reply.TextUrlMsg_news(to_User, from_User, return_content, picurl, url)
                        return replyMsg.send()
                    elif Levenshtein.similar_music(user_content) == True:
                        redis_db.set(to_User, 'music_serving')

                        return_content = r'''
    您已开启网易云音乐功能，输入歌曲或歌手开始搜索！
    注意：歌曲名称避免出现 # 操作符
    #q : 退出'''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif Levenshtein.similar_movie(user_content) == True:
                        redis_db.set(to_User, 'movie_serving')
                        if redis_db.get('cinema_info'):
                            pass
                        else:
                            redis_db.set('cinema_info', movie_Finance.cinema())
                        # print u"状态更改-->" + redis_db.get(to_User + '-music_server')
                        return_content = r'''
    欢迎使用电影数据包，您可以查看最新的全国票房以及影院信息
    #1 : 查询电影票房
    #2 : 查询影院信息(前十名)
    #q : 退出'''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif Levenshtein.similar_wxRobot(user_content) == True:
                        redis_db.set(to_User, 'wxRobot_serving')

                        return_content = r'''
    微信个人号机器人服务请求界面
    Miss Paprika会托管你的微信消息处理

    #1 : 自定义自动回复
    #2 : 申请好友自动添加
    #3 : 聊天机器人
    #4 : 查看删除自己的好友
    #5 : 微信好友信息统计
    #6 : 撤回消息查看
    #q : 退出

    提醒 : 请低频率使用该功能，防止微信封号！最糟糕情况是无法登陆网页微信，但是手机端和桌面版不会受到影响
    '''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif Levenshtein.similar_email(user_content) == True:
                        redis_db.set(to_User, 'email_serving')
                        return_content = r'''
    欢迎使用邮件服务

    #1 : 匿名邮件
    #2 : QQ邮件代理发送
    #q : 退出
                            '''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif to_User == 'oHfuz0hYUIrqM6b410E7nK8TnlGE' and user_content == 'admin':
                        redis_db.set(to_User, 'admin_serving')

                        return_content = r'''
    孙合庆您好！当前是管理员控制面板

    #1 : 激活Hunter,抓取新闻数据
    #2 : 激活Time_Task_Manager
    #3 : 发送异常日志
    #4 : 公告
    #5 : 调整模糊匹配度
    #q : 退出管理员界面

                    '''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif user_content == '#about':
                        return_content = r'''
    公示牌
                        '''+redis_db.get('about_text')+'\n'+r'''
    开发者 : 城市牛仔

    意见/需求 反馈?
    WeChat : manzhouren123
    E-mail : 2436437774@qq.com

    商业洽谈？
    TEL : 18810579785
                        '''+'\n'+norm_text.hi_2_text

                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    else:
                        return_content = tuling_reply.tuling_reply(user_content)
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()


                # 负责音乐会话的控制，真的不想写这么多if elif 啊！好low啊。。。。
                #####################
                elif redis_db.get(to_User) == 'music_serving':
                    if '#' not in user_content:
                        music_list = netease_music.WXmusic(user_content)
                        redis_db.set(to_User + '-music_server_content', music_list[1])
                        return_content = u'搜索结果，输入歌曲的#码选择歌曲' + '\n' + u'例如  #2 选择第二首' + '\n\n' + '\n'.join(
                            music_list[0])
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif user_content == "#q":
                        redis_db.set(to_User, 'other_serving')
                        return_content = u"您已关闭网易云音乐功能！"
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    else:
                        num = int(user_content.replace('#', '')) - 1
                        print num
                        id_list = eval(redis_db.get(to_User + '-music_server_content'))
                        id = id_list[num]
                        print id
                        music_url = netease_music.WXmusic_search(id)
                        replyMsg = reply.TextUrlMsg_music(to_User, from_User, music_url)
                        print replyMsg
                        return replyMsg.send()
                #####################

                # 负责电影会话的控制
                #####################
                elif redis_db.get(to_User) == 'movie_serving':

                    if user_content == '#1':
                        if redis_db.get('movie_info'):
                            pass
                        else:
                            redis_db.set('movie_info', movie_Finance.movie())
                        return_content = redis_db.get('movie_info')  # 这个需要缓存
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif user_content == '#2':
                        return_content = redis_db.get('cinema_info')
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif user_content == "#q":
                        redis_db.set(to_User, 'other_serving')
                        return_content = u"您已关闭电影数据包！"
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    else:
                        return_content = r'''
    输入错误！提示：
    #1 : 查询电影票房
    #2 : 查询影院信息(前十名)
    #q : 退出'''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                #####################

                # 负责邮件会话的控制
                #####################
                elif redis_db.get(to_User) == 'email_serving':

                    if user_content == '#1':
                        redis_db.set(to_User, 'email_serving_sending')
                        redis_db.set(to_User+'email_serving_sending', 'title')
                        return_content =   r'''
    邮件发送界面

    按照提示依次输入：邮件标题、邮件正文、目标邮箱
    #q : 退出

    首先输入邮件标题：'''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif user_content == '#2':
                        return_content = redis_db.get('cinema_info')
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif user_content == "#q":
                        redis_db.set(to_User, 'other_serving')
                        return_content = u"您已关闭邮件服务！"
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    else:
                        return_content = r'''
    输入错误！提示：

    #1 : 匿名邮件
    #2 : QQ邮件代理发送
    #q : 退出'''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                elif redis_db.get(to_User) == 'email_serving_sending':
                    if user_content == "#q":
                        redis_db.set(to_User, 'other_serving')
                        return_content = u"您已关闭邮件服务！"
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif redis_db.get(to_User+'email_serving_sending') == 'title':
                        redis_db.set(to_User+'email_serving_sending', 'content')
                        redis_db.set(to_User + 'email_caching', user_content+to_User)
                        return_content = r'''
    邮件发送界面

    #q : 退出

    请输入邮件正文：
                '''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif redis_db.get(to_User+'email_serving_sending') == 'content':
                        redis_db.set(to_User + 'email_serving_sending', 'email')
                        caching = redis_db.get(to_User + 'email_caching')+user_content
                        redis_db.set(to_User + 'email_caching', caching)
                        return_content = r'''
    邮件发送界面

    #q : 退出

    请输入目标邮箱：
                '''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif redis_db.get(to_User + 'email_serving_sending') == 'email':
                        redis_db.set(to_User, 'other_serving')
                        caching_list = redis_db.get(to_User + 'email_caching').split(to_User)
                        email_dict = {}
                        email_dict['type'] = 'email'
                        email_dict['from_user'] = '2436437774@qq.com'
                        email_dict['to_user'] = user_content
                        email_dict['email_key'] = 'rjzitqsxhqmyebid'
                        email_dict['title'] = caching_list[0]
                        email_dict['content'] = caching_list[-1]
                        redis_db.set(to_User + 'email_caching', email_dict)
                        self.rcon.lpush(self.prodcons_queue, email_dict)
                        return_content = r'''
    邮件发送界面'''+'\n'+r'''邮件标题：'''+caching_list[0]+'\n'+r'''邮件正文：'''+caching_list[-1]+'\n'+r'''目标邮箱：'''+user_content+'''

    已经自动退出邮件发送界面
            '''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()


                    else:
                        return_content = r'''
    输入错误！提示：

    认真查看服务代码提示
    #q : 退出
            '''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                #####################

                # 负责请求微信机器人服务会话的控制
                #####################

                elif redis_db.get(to_User) == 'wxRobot_serving':

                    if user_content == '#1':
                        redis_db.set(to_User, 'wxRobot_serving_1')
                        return_content = r'''告诉我你的自定义回复内容'''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif user_content == '#2':
                        return_content = 'test'
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif user_content == "#q":
                        redis_db.set(to_User, 'other_serving')
                        return_content = u"您已关闭微信机器人服务请求！"
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    else:
                        return_content = r'''
    输入错误！提示：

    #1 : 自定义自动回复
    #2 : 申请好友自动添加
    #3 : 语音聊天机器人
    #4 : 查看删除自己的好友
    #5 : 微信好友信息统计
    #6 : 撤回消息查看
    #q : 退出
    '''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                elif redis_db.get(to_User) == 'wxRobot_serving_1':  #发送自定义信息
                    redis_db.set(to_User, 'wxRobot_serving_1_1')   #用户下一步进入子会话的子会话
                    queue_dict = {}
                    queue_dict['text'] = user_content
                    queue_dict['user_id'] = to_User
                    queue_dict['type'] = 'auto_reply'
                    self.rcon.lpush(self.prodcons_queue, queue_dict) # 消息队列启动服务
                    return_content = r'''
    Hi! 我就是Paprika，我收到了你的自动回复信息
    自动回复消息为：''' + user_content + r'''

    #1 : 更改自动回复信息
    #2 : 启动服务（扫描我们发送给您的二维码）
    #q : 退出
    您可以通过退出网页端微信关闭该功能''' + '\n' + norm_text.subscribe_text
                    replyMsg = reply.TextMsg(to_User, from_User, return_content)
                    return replyMsg.send()
                elif redis_db.get(to_User) == 'wxRobot_serving_1_1':

                    if user_content == '#1':
                        redis_db.set(to_User, 'wxRobot_serving_1')
                        return_content = '''重新告诉我你的自定义回复内容'''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif user_content == '#2':  #通过消息队列启动服务（实际服务已经启动，这里是扫码）
                        return_content = 'test'
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif user_content == "#q":
                        redis_db.set(to_User, 'wxRobot_serving')
                        return_content = u"您已关闭自定义回复功能，已返回至微信机器人服务请求界面！"
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    else:
                        return_content = r'''
    输入错误！提示：

    #1 : 更改自动回复信息
    #2 : 启动服务（扫描我们发送给您的二维码）
    #q : 退出
                '''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                #####################

                # 负责管理员会话的控制
                #####################
                elif redis_db.get(to_User) == 'admin_serving':

                    if user_content == '#1':
                        queue_dict = {}
                        queue_dict['text'] = 'Hunter'
                        queue_dict['user_id'] = to_User
                        self.rcon.lpush(self.prodcons_queue, queue_dict)
                        return_content = '已激活Hunter'
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif user_content == '#4':
                        redis_db.set(to_User, 'admin_serving_4')
                        return_content = r'''请输入公告内容！（执行完毕即退回上级目录）'''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    elif user_content == "#q":
                        redis_db.set(to_User, 'other_serving')
                        return_content = u"您已关闭控制面板！"
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                    else:
                        return_content = r'''
    输入错误！提示：
    #1 : 激活Hunter,抓取新闻数据
    #2 : 激活Time_Task_Manager
    #3 : 发送异常日志
    #4 : 公告
    #5 : 调整模糊匹配度
    #q : 退出'''
                        replyMsg = reply.TextMsg(to_User, from_User, return_content)
                        return replyMsg.send()
                elif redis_db.get(to_User) == 'admin_serving_4':
                    redis_db.set('about_text', user_content)
                    redis_db.set(to_User, 'admin_serving')
                    return_content = r'''
    公告写入成功！
    #about 查看公告
    已经返回至管理员界面'''
                    replyMsg = reply.TextMsg(to_User, from_User, return_content)
                    return replyMsg.send()
                #####################
                else:
                    # redis 出现异常时候可能会用到
                    return_content = r'''
    奥谭出现异常！目前是机器人托管状态
    机器人：
        '''+tuling_reply.tuling_reply(user_content)
                    replyMsg = reply.TextMsg(to_User, from_User, return_content)
                    return replyMsg.send()


            else:
                to_User = recMsg.FromUserName
                from_User = recMsg.ToUserName
                user_content = '?'
                return_content = tuling_reply.tuling_reply(user_content)
                replyMsg = reply.TextMsg(to_User, from_User, return_content)
                return replyMsg.send()

        except Exception, Argment:
            return Argment
