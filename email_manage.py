# -*- coding: utf-8 -*-
# @Author : qinlei
# @Time : 2022/8/7 8:37 下午
# @Function:
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailManage:

    def send_email(self):
        #定义SMTP服务器是什么
        smtpserver = "smtp.qq.com"
        # 授权码
        username = "2252926079@qq.com"
        password = "vepmmzupdaifeceh"

        receiver = "13081850733@163.com"

        # 创建邮件对象
        message = MIMEMultipart('related')
        subject = '湖南省网通项目测试报告'
        # fujian = MIMEText(open('test.txt', 'rb').read(), 'txt', 'utf-8') # 附件

        # 组装到邮件对象中
        message['from'] = username
        message['to'] = receiver
        message['subject'] = subject

        # 登录smtp服务器
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(username, receiver, message.as_string())
        smtp.quit()