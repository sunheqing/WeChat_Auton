#coding=utf-8
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.application import MIMEApplication
# from email.header import Header
import smtplib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
type=sys.getfilesystemencoding()
'''
class email:
    def __int__(self,to_user,email_title,email_text,from_user, key):
        self.to_user=to_user
        self.email_title=email_title
        self.email_text=email_text
        self.from_user = from_user
        self.key = key
        '''
def email_send(email_title,email_text,to_user, from_user, key):
    msg = MIMEMultipart('mixed')
    msg['Subject'] =email_title
    msg['From'] = '微信助手代理邮箱'
    msg['To'] = to_user
    msg['Data'] = time.ctime()
    text = email_text
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)
    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.set_debuglevel(1)
    smtp.login(from_user, key)
    smtp.sendmail(from_user, [from_user, to_user], msg.as_string())
    smtp.quit()