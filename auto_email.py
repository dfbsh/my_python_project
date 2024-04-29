import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # 设置邮箱服务器地址和端口
    smtp_server = 'smtp.qq.com'
    port = 587  # 一般是587端口

    # 创建一个 SMTP 连接
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # 开启安全连接

    # 登录邮箱
    server.login(sender_email, sender_password)

    # 创建一个 MIMEMultipart 对象
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(message, 'plain'))

    # 发送邮件
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # 关闭连接
    server.quit()

# 设置发件人邮箱和密码
sender_email = '1293086005@qq.com'
sender_password = 'ufvbqnjbrlnxijff'

# 设置收件人邮箱
receiver_email = 'receiver@example.com'

# 设置邮件主题和内容
subject = 'Test Email'
message = 'Hello, this is a test email!'

# 调用函数发送邮件
send_email(sender_email, sender_password, receiver_email, subject, message)
#ufvbqnjbrlnxijff