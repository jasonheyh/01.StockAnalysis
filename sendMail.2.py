# encoding: utf-8
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header

def send_email(SMTP_host, from_addr, password, to_addrs, subject, content):
    email_client = SMTP(SMTP_host,25)
    email_client.login(from_addr, password)
    # create msg
    msg = MIMEText(content,'plain','utf-8')
    msg['Subject'] = Header(subject, 'utf-8')#subject
    msg['From'] = 'heyonghan@163.com'
    msg['To'] = "heyonghan@163.com"
    email_client.sendmail(from_addr, to_addrs, msg.as_string())

    email_client.quit()

if __name__ == "__main__":
    send_email("9.119.104.138","heyonghan@163.com","163zaq12wsx","heyonghan@163.com","2saas","hellow")