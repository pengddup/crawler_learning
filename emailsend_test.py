# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# 写成了一个通用的函数接口，想直接用的话，把参数的注释去掉就好
def sen_email(msg_from, passwd, msg_to, text_content, file_path=None):
    msg_from = '214018554@qq.com'  # 发送方邮箱
    passwd = 'tnjdsqevcgsrbice'  # 填入发送方邮箱的授权码（就是刚刚你拿到的那个授权码）
    msg_to = '849099690@qq.com'  # 收件人邮箱

    msg = MIMEMultipart()

    subject = "彭文剑本周工作总结与下周工作计划-20190930"  # 主题
    text_content = "杨总：下午好！这是是我这周的工作总结及下周的工作计划，请查收。-----------------彭文剑TEL:18575682917"

    text = MIMEText(text_content)
    msg.attach(text)

    docFile = r'E:\2017-2019xinaonet\工作记录\周报\彭文剑本周工作总结与下周工作计划-20190930.xlsx'  #如果需要添加附件，就给定路径
    if file_path(docFile):  # 最开始的函数参数我默认设置了None ，想添加附件，自行更改一下就好
        docFile = file_path
        docApart = MIMEApplication(open(docFile, 'rb').read())
        docApart.add_header('Content-Disposition', 'attachment', filename=docFile)
        msg.attach(docApart)

    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print('发送成功')


