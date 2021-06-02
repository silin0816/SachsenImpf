# !/user/bin/env python
# -*- coding:utf-8 -*-
# author: silin yang
# date: 29.05.2021

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import winsound


# def send_email():
#     msg_from = '914373315@qq.com'  # from
#     passwd = 'vahcqdhmcogfbfjc'
#     to = ['914373315@qq.com']  # to
#     msg = MIMEMultipart()
#     content = "！！！！有termin啦！！！！"  # content
#     msg.attach(MIMEText(content, 'plain', 'utf-8'))
#     msg['Subject'] = "Corona"
#     msg['From'] = msg_from
#     s = smtplib.SMTP_SSL("smtp.qq.com", 465)
#     s.login(msg_from, passwd)
#     # send
#     s.sendmail(msg_from, to, msg.as_string())
#     print("邮件发送成功")

class GetTermin():
    def __init__(self, PATH):
        self.driver = webdriver.Chrome(PATH)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """                                                                        
                  Object.defineProperty(navigator, 'webdriver', {                                    
                    get: () => undefined                                                             
                  })                                                                                 
                """
        })  # })
        self.driver.get("https://sachsen.impfterminvergabe.de/civ.public/start.html?oe=00.00.IM&mode=cc&cc_key=IOAktion")

    def waiting_login(self):
        # wait until the entrance appears
        try:
            wait = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.ID, "gwt-uid-3")))
        finally:
            print('open pages')
        return self

    def update_terimin(self):
        while True:
            self.driver.find_element_by_id('WorkflowButton-4212').click()
            time.sleep(5)
            try:
                self.driver.find_element_by_class_name('sjf-step-intro')
                self.driver.find_element_by_id("WorkflowButton-4255").click()
                time.sleep(5)
            except:
                winsound.Beep(600, 8000)
                # send_email()
                break


    def login(self, account, pwd):
        self.waiting_login()
        time.sleep(2)
        _item1 = self.driver.find_element(By.ID, "gwt-uid-3")
        self.driver.execute_script("arguments[0].click();", _item1)
        self.driver.find_element(By.ID, "gwt-uid-3").send_keys(account)
        _item2 = self.driver.find_element(By.ID, "gwt-uid-5")
        self.driver.execute_script("arguments[0].click();", _item2)
        self.driver.find_element(By.ID, "gwt-uid-5").send_keys(pwd)
        self.driver.find_element(By.CSS_SELECTOR, "#WorkflowButton-4212 > span").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".gwt-RadioButton:nth-child(2) > label").click()
        self.driver.find_element(By.CSS_SELECTOR, "#WorkflowButton-4212 > span").click()
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, 'selection').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li[6]').click()

        time.sleep(2)
        self.update_terimin()



if __name__ == '__main__':

    ACCOUNT = "A204-36513"
    PWD = "yin940319"
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    GetTermin(PATH).login(ACCOUNT, PWD)






