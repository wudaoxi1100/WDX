#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib

#小文件可以直接打开    
#with open('E:\操作系统镜像\win2012激活工具.iso','rb') as file1:
#    context=file1.read()

#大文件需要拆分读取
def cal_md5(word):
    if isinstance(word,str):
        word=word.encode('utf-8')
    print('sss')
    return word

md5 = hashlib.md5()    
maxbuf=8192  #每次读取8KB   
with open(r'C:\Users\WDX\Desktop\test.txt','rb') as file1:  
    while True:
        buf = file1.read(maxbuf)  #依次读取
        if not buf:
            break
        md5.update(cal_md5(buf))
        
hash = md5.hexdigest()
print(hash)