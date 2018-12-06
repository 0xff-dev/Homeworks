import os
import base64
from socket import *


# 参考https://blog.csdn.net/u012302681/article/details/33699077
# 明天回来重新整理代码, 今天先跑通
# 代码中的aim_mail 替换成接受者的邮箱

class email(object):
    
    def __init__(self):
        self.environs = os.environ
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(('smtp.163.com', 25))
        self.user = base64.b64encode(self.environs['MAIL'].encode('utf-8')).decode('utf-8')
        self.pwd = base64.b64encode(self.environs['PWD'].encode('utf-8')).decode('utf-8')

    def test(self):
        recv = self.client.recv(1024).decode('utf-8')
        print(recv)
        if recv[:3] != '220':
            print("服务器没有准备好")
    def helo(self):
        self.client.send('HELO Hi\r\n'.encode('utf-8'))
        recv = self.client.recv(1024).decode()
        if recv[:3] != '250':
            print("打招呼失败")

    def auth_login(self):
        self.client.send('AUTH LOGIN\r\n'.encode('utf-8'))
        recv = self.client.recv(1024).decode('utf-8')
        if recv[:3] != '334':
            print('请求认证失败')

    def send_userinfo(self):
        self.client.send((self.user+'\r\n').encode('utf-8'))
        recv = self.client.recv(1024).decode('utf-8')
        if recv[:3] != '334':
            print('用户名认证失败')

        self.client.send((self.pwd+'\r\n').encode('utf-8'))
        recv = self.client.recv(1024).decode('utf-8')
        if recv[:3] != '235':
            print('密码验证失败')

    def send_mail(self):
        self.test()
        self.helo()
        self.auth_login()
        self.send_userinfo()
        self.client.send('MAIL FROM: <{}>\r\n'.format(self.environs['MAIL']).encode('utf-8'))
        recv = self.client.recv(1024).decode('utf-8')
        if recv[:3] != '250':
            print("发送MAIL FROM 失败")

        self.client.send('RCPT TO: <aim_mail>\r\n'.encode('utf-8'))
        recv = self.client.recv(1024).decode('utf-8')
        if recv[:3] != '250':
            print('RCPT TO 发送失败')

        self.client.send('DATA\r\n'.encode('utf-8'))
        recv = self.client.recv(1024).decode('utf-8')
        if recv[:3] != '354':
            print('data  请求失败')

        message = 'from:' + self.environs['MAIL'] + '\r\n'
        message += 'to:' + '935809546@qq.com' + '\r\n'
        message += 'subject:' + '自己连接server' + '\r\n'
        message += 'Content-Type:' + 'text/plain' + '\t\n'
        self.client.sendall(message.encode('utf-8'))

        self.client.send('\r\n.\r\n'.encode('utf-8'))
        recv = self.client.recv(1024).decode('utf-8')
        if recv[:3] != '250':
            print('发送失败')
        else:
            print('发送成功')

        self.client.send('QUIT\r\n'.encode('utf-8'))
        self.client.close()


if __name__ == '__main__':
    mail = email()
    mail.send_mail()
