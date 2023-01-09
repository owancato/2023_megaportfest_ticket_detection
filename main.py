# This is a sample Python script.
import requests
from bs4 import BeautifulSoup
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get(url):
    response = requests.get(url)
    return response

def send_email(msg):
    content = MIMEMultipart()  # 建立MIMEMultipart物件
    content["subject"] = "搶票囉"  # 郵件標題
    content["from"] = "your_email"  # 寄件者
    content["to"] = "email1, email2, ..."  # 收件者
    content.attach(MIMEText(msg))  # 郵件內容
    pwd = '' # 你的google應用程式密碼
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("your_email", pwd)  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ticket_name = [
        '全區(雙日聯票)',
        '全區(雙日毛巾套票)',
        '全區(4/1單日票)',
        '全區(4/2一般單日)'
    ]
    while(True):
        res = get('https://tixcraft.com/ticket/area/23_megaport/13729')
        soup = BeautifulSoup(res.text, "html.parser")
        tickets = [soup.find(id="group_20944").find('font').text,
                   soup.find(id="group_20945").find('font').text,
                   soup.find(id="group_20946").find('font').text,
                   soup.find(id="group_20947").find('font').text]
        for i in range(len(tickets)):
            if tickets[i].find('Sold out') == -1:
                msg = ticket_name[i]+" 有空缺\n 給你連結 快去搶\n https://tixcraft.com/ticket/area/23_megaport/13729"
                print(msg)
                send_email(msg)
        time.sleep(3)
