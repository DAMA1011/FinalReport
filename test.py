<<<<<<< HEAD
# 操作 browser 的 API
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 處理逾時例外的工具
from selenium.common.exceptions import TimeoutException

# 處理找不到元素的工具
from selenium.common.exceptions import NoSuchElementException

# 面對動態網頁，等待某個元素出現的工具，通常與 exptected_conditions 搭配
from selenium.webdriver.support.ui import WebDriverWait

# 搭配 WebDriverWait 使用，對元素狀態的一種期待條件，若條件發生，則等待結束，往下一行執行
from selenium.webdriver.support import expected_conditions as EC

# 期待元素出現要透過什麼方式指定，通常與 EC、WebDriverWait 一起使用
from selenium.webdriver.common.by import By

# 加入行為鍊 ActionChain (在 WebDriver 中模擬滑鼠移動、點繫、拖曳、按右鍵出現選單，以及鍵盤輸入文字、按下鍵盤上的按鈕等)
from selenium.webdriver.common.action_chains import ActionChains

# 加入鍵盤功能 (例如 Ctrl、Alt 等)
from selenium.webdriver.common.keys import Keys

# 強制等待 (執行期間休息一下)
import time
from time import sleep

# 匯入 regex 套件
import re

# 整理 json 使用的工具
import json, csv

# 讓顯示好讀
import pprint

# 平行任務處理
from concurrent.futures import ProcessPoolExecutor as ppe

nameList = []  # 存放首頁查詢滾動完的所有店家資訊網址

dataList = []  # 存放各個店家的目標資訊

# 啟動瀏覽器的工具選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")  # 不開啟實體瀏覽器背景執行
my_options.add_argument('--disable-gpu')  # 關閉 GPU，避免某些系統或是網頁出錯
# my_options.add_argument("--start-maximized")  # 最大化視窗
# my_options.add_argument('window-size=1920,1080')
my_options.add_argument("--incognito")  # 開啟無痕模式
my_options.add_argument("--disable-popup-blocking")  # 禁用彈出攔截
my_options.add_argument("--disable-notifications")  # 取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  # 設定為正體中文
my_options.add_experimental_option("detach", True)
my_options.add_experimental_option('excludeSwitches', ['enable-logging'])
my_service = Service(ChromeDriverManager().install())


driver = webdriver.Chrome(options = my_options, service = my_service)

with open('大同區String.csv', 'r') as csvfile:

    rows = csv.reader(csvfile, delimiter=' ')

    row = list(rows)

for i in range(len(row)):
    
    driver.get(row[i][0])
=======
import pandas as pd
import numpy as np


df = pd.read_csv('attraction_info_final_1213.csv', encoding='utf-8')

# print(df.isnull().values.any())

# print(df.isna().values.any())

# print(df.columns)

df2 = df.replace({np.nan:None})

# print(df2.isna().values.any())

for i,row in df2.iterrows():
    print(row)
>>>>>>> a8a150968634cce942626ff77b8ed9ca306059f6
