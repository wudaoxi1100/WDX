#!/usr/bin/env python3
#-*-coding:utf-8 -*-

import socket,threading,time
wdx='sd'
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
    
ss=1
sdsd='pj'