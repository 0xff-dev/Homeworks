#!/usr/bin/env python
# coding=utf-8
import os
import base64
from socket import *


# 参考https://blog.csdn.net/u012302681/article/details/33699077
# 明天回来重新整理代码, 今天先跑通
# 代码中的aim_mail 替换成接受者的邮箱

environs = os.environ
client = socket(AF_INET, SOCK_STREAM)
client.connect(('smtp.163.com', 25))

user = base64.b64encode(environs['MAIL'].encode('utf-8')).decode('utf-8')
pwd = base64.b64encode(environs['PWD'].encode('utf-8')).decode('utf-8')


recv = client.recv(1024).decode('utf-8')
print(recv)
if recv[:3] != '220':
    print("服务器没有准备好")

client.send('HELO Hi\r\n'.encode('utf-8'))
recv = client.recv(1024).decode()
if recv[:3] != '250':
    print("打招呼失败")

client.send('AUTH LOGIN\r\n'.encode('utf-8'))
recv = client.recv(1024).decode('utf-8')
if recv[:3] != '334':
    print('请求认证失败')

client.send((user+'\r\n').encode('utf-8'))
recv = client.recv(1024).decode('utf-8')
if recv[:3] != '334':
    print('用户名认证失败')

client.send((pwd+'\r\n').encode('utf-8'))
recv = client.recv(1024).decode('utf-8')
if recv[:3] != '235':
    print('密码验证失败')

client.send('MAIL FROM: <{}>\r\n'.format(environs['MAIL']).encode('utf-8'))
recv = client.recv(1024).decode('utf-8')
if recv[:3] != '250':
    print("发送MAIL FROM 失败")

client.send('RCPT TO: <aim_mail>\r\n'.encode('utf-8'))
recv = client.recv(1024).decode('utf-8')
if recv[:3] != '250':
    print('RCPT TO 发送失败')

client.send('DATA\r\n'.encode('utf-8'))
recv = client.recv(1024).decode('utf-8')
if recv[:3] != '354':
    print('data  请求失败')

message = 'from:' + environs['MAIL'] + '\r\n'
message += 'to:' + 'aim_mail' + '\r\n'
message += 'subject:' + '自己连接server' + '\r\n'
message += 'Content-Type:' + 'text/plain' + '\t\n'
client.sendall(message.encode('utf-8'))

client.send('\r\n.\r\n'.encode('utf-8'))
recv = client.recv(1024).decode('utf-8')
if recv[:3] != '250':
    print('发送失败')
else:
    print('发送成功')

client.send('QUIT\r\n'.encode('utf-8'))
client.close()
