# coding:utf-8

import socket   # 导入 socket 模块


def test_server():
    s = socket.socket()  # 创建 socket 对象

    host = socket.gethostname()  # 获取本地主机名
    port = 80  # 设置端口
    addr = (host, port)  # 设置地址tuple
    s.bind(addr)  # 绑定端口

    s.listen(10)  # 等待客户端连接
    while True:
        c, addr = s.accept()  # 接收客户端的连接
        print '连接地址：', addr
        c.send('this is a test!')
        #print s.recv(1024)
        c.close()  # 关闭连接

test_server()