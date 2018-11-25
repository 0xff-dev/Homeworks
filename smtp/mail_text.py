import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Smtp(object):

    def __init__(self):
        self.enviros = os.environ
        self.host = 'smtp.163.com'
        self.mail_user = self.enviros['MAIL']
        self.mail_pwd = self.enviros['PWD']
        self.sender = self.enviros['MAIL']

    def send_mail(self):
        receivers = input("接受者, 以空格分割: ")
        receivers = receivers.split(' ')
        title = input("邮件标题: ")
        content = input("邮件征文: ")
        msg = MIMEText(content, "plain", "utf-8")
        msg['From'] = self.mail_user
        msg['To'] = ','.join(receivers)
        msg['Subject'] = Header(title, 'utf-8')
        try:
            self.smtp = smtplib.SMTP()
            self.smtp.connect(host=self.host, port=25)
            self.smtp.login(self.mail_user, self.mail_pwd)
            self.smtp.sendmail(self.sender, receivers, msg.as_string())
        except smtplib.SMTPException as e:
            print(e.args)

smtp = Smtp()
smtp.send_mail()