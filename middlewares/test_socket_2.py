# coding:utf-8

import socket   # 导入 socket 模块

def test_client():
    s = socket.socket()  # 创建 socket 对象
    host = '192.168.1.103'  # 获取本地主机名
    port = 80  # 设置端口
    addr = (host, port)
    s.connect(addr)  # 绑定端口号
    #c, addr = s.accept()  # 接收客户端的连接
    #print '连接地址：', addr
    #c.send('this is a test!')
    print s.recv(1024)  # 打印接收的数据
    s.close()  # 关闭连接
test_client()