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
import json

# 執行 command 的時候用的
import pprint

# 啟動瀏覽器工具的選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")  #不開啟實體瀏覽器背景執行
# my_options.add_argument("--start-maximized")  #最大化視窗
my_options.add_argument("--incognito")  #開啟無痕模式
my_options.add_argument("--disable-popup-blocking")  #禁用彈出攔截
my_options.add_argument("--disable-notifications")  #取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  #設定為正體中文

# 使用 Chrome 的 WebDriver
driver = webdriver.Chrome(
    options = my_options,
    service = Service(ChromeDriverManager().install())
)

dataList = []

driver.get('https://www.google.com.tw/maps/place/%E9%BB%9E%E5%AD%90%E6%97%A9%E5%8D%88%E9%A4%90/@25.0674675,121.5086235,17z/data=!4m5!3m4!1s0x3442a94a0a5cc503:0xd227cecd64ac1bd8!8m2!3d25.0693149!4d121.5094486?hl=zh-TW')

# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located(
#         (By.CSS_SELECTOR, 'div[data-js-log-root][role="region"] div[data-js-log-root] button[data-item-id="oloc"] div[style^=font-family]')
#     )
# )

# # 查詢是否符合士林區、大同區
# type = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root][role="region"] div[data-js-log-root] button[data-item-id="oloc"] div[style^=font-family]')
# regex = r'.*大同區.*'
# result = re.match(regex, type.get_attribute('innerText'))
# if result != None:
# try:
#     # 店名
#     place_name = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] h1 span').get_attribute('innerText')
# except NoSuchElementException:
#     place_name = ""
#     pass

# try:
#     # 星數
#     total_rating = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] span[aria-hidden="true"]').get_attribute('innerText')
# except NoSuchElementException:
#     total_rating = ""
#     pass

# try:
#     # 地點標籤、類別
#     place_category = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] div[data-js-log-root] div[style^="font-family"] > span button[jsaction][jstcache][class][jsan]').get_attribute('innerText')
# except NoSuchElementException:
#     place_category = ""
#     pass

# try:
#     # 評論數
#     total_reviews = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] div[data-js-log-root] div[style^="font-family"] div[role="button"] span[style] span[aria-label][jstcache][jsan]').get_attribute('innerText')
# except NoSuchElementException:
#     total_reviews = ""
#     pass

# try:
#     # 消費水平
#     cost = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] span[aria-label^="價格"]').get_attribute('innerText')
# except NoSuchElementException:
#     cost = ""
#     pass

# try:
#     # 地址
#     address = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] [role="region"] div[data-js-log-root] button[data-item-id="address"] div[style^=font-family]').get_attribute('innerText')
# except NoSuchElementException:
#     address = ""
#     pass

try:
    # 行政區
    district = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button[aria-label^=Plus] div[style^=font-family]').get_attribute('innerText')
except NoSuchElementException:
    district = ""
    

# 提供內用(boolean)
try:
    driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button div[style^="font-family"] div[aria-label="提供內用"]')
    eat_in = 1
except NoSuchElementException:
    eat_in = 0
                    
# 提供外帶服務(boolean)
try:
    driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button div[style^="font-family"] div[aria-label="提供外帶服務"]')
    to_go_1 = 1
except NoSuchElementException:
    to_go_1 = 0
            
# 提供路邊取餐服務(boolean)
try:
    driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button div[style^="font-family"] div[aria-label="提供路邊取餐服務"]')
    to_go_2 = 1
except NoSuchElementException:
    to_go_2 = 0

# 提供外送服務(boolean)
try:
    driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button div[style^="font-family"] div[aria-label="提供外送服務"]')
    delivery = 1
except NoSuchElementException:
    delivery = 0

# try:
#     # 營業時間
#     opening_hour = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root][role="region"] div[data-js-log-root][style^=font-family] div[aria-label]').get_attribute('aria-label')
# except NoSuchElementException:
#     opening_hour = ""
#     pass

# try:
#     # 景點店家官網
#     website = driver.find_element(By.CSS_SELECTOR, 'div[role="region"] a[data-item-id="authority"][href]').get_attribute('href')
# except NoSuchElementException:
#     website = ""
#     pass

try:
    # 景點店家電話
    phone = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button[aria-label^=電話號碼] div[style^=font-family]').get_attribute('innerText')
except NoSuchElementException:
    phone = ""
    

try:
    # 是否關閉
    close = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] div[data-js-log-root] div[style^="font-family"] span[style="color:#D93025"] span').get_attribute('innerText')
except NoSuchElementException:
    close = ""
    

    # 爬取地點資料當天的日期
    t = time.time()
    place_acquisition_date = time.ctime(t)

# print('=' * 200)

dataList.append({
    # 'google_url': nameList[i],  # google maps網址
    # 'place_name': place_name,  # 店名
    # 'total_rating': total_rating,  # 星數
    # 'place_category': place_category,  # 地點標籤、類別
    # 'total_reviews': total_reviews,  # 評論數
    # 'cost': cost,  # 消費水平
    # 'address': address,  # 地址
    'district': district,  # 行政區
    'eat_in': eat_in,  # 提供內用(boolean)
    'to_go_1': to_go_1,  # 提供外帶服務(boolean)
    'to_go_2': to_go_2,  # 提供路邊取餐服務(boolean)
    'delivery': delivery,  # 提供外送服務(boolean)
    # 'opening_hour': opening_hour,  # 營業時間
    # 'website': website,  # 景點店家官網
    'phone': phone,  # 景點店家電話
    'close': close,  # 是否關閉
    'place_acquisition_date': place_acquisition_date  # 爬取地點資料當天的日期
})

sleep(0.5)

pprint.pprint(dataList)