# 2023_大港票庫存偵測程式

## 前置作業

### 安裝python

### 安裝套件
```
pip install beautifulsoap4
pip install request
```

## 如何使用
### 在 main.py 裡面填入信箱、應用程式密碼等相關資訊
```
content["from"] = "your_email"  # 寄件者
content["to"] = "email1, email2, ..."  # 收件者
pwd = '' # 你的google應用程式密碼
smtp.login("your_email", pwd)  # 登入寄件者gmail
```

### 執行程式
```
python3 main.py
```
