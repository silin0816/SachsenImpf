# !/user/bin/env python
# -*- coding:utf-8 -*-
# author: silin yang
# date: 29.05.2021

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import winsound
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# open the website
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """                                                                        
      Object.defineProperty(navigator, 'webdriver', {                                    
        get: () => undefined                                                             
      })                                                                                 
    """
  })

def send_email():
    msg_from = '914373315@qq.com'  # from
    passwd = 'vahcqdhmcogfbfjc'
    to = ['914373315@qq.com']  # to
    msg = MIMEMultipart()
    content = "！！！！有termin啦！！！！"  # content
    msg.attach(MIMEText(content, 'plain', 'utf-8'))
    msg['Subject'] = "Corona"
    msg['From'] = msg_from
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(msg_from, passwd)
    # send
    s.sendmail(msg_from, to, msg.as_string())
    print("邮件发送成功")

while(True):
    weiter_button = driver.find_element_by_id('WorkflowButton-4212').click()
    time.sleep(10)
    condition = driver.find_element_by_class_name('sjf-step-intro').text
    text = 'Aufgrund der aktuellen Auslastung der Impfzentren und der verfügbaren Impfstoffmenge können wir Ihnen leider' \
           ' keinen Termin anbieten. Bitte versuchen Sie es in ein paar Tagen erneut.'
    if condition == text:
        back_button = driver.find_element_by_id("WorkflowButton-4255").click()
        time.sleep(5)
    else:
        winsound.Beep(600,8000)
        send_email()
        break


