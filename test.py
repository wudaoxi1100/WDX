#!/usr/bin/env python3
#-*-coding:utf-8 -*-

import socket,threading,time

def tcplink(sock,addr):
   # print(sock)i
    print('Accept form %s:%s' % addr)  #addr是一个tuple,有2个字段
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s closed' % addr[0])
    
#creat a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#监听端口
s.bind(('192.168.57.1',9999))
s.listen(5)     #制定等待连接的最大数量
print ('Waiting for connecting...')
while True:
    sock, addr = s.accept()
    #创建新线程来处理
    t = threading.Thread(target = tcplink,args=(sock,addr))
    t.start()
    
    

        