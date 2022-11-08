# 操作 browser 的 API
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 處理逾時例外的工具
from selenium.common.exceptions import TimeoutException

# 面對動態網頁，等待某個元素出現的工具，通常與 exptected_conditions 搭配
from selenium.webdriver.support.ui import WebDriverWait

# 搭配 WebDriverWait 使用，對元素狀態的一種期待條件，若條件發生，則等待結束，往下一行執行
from selenium.webdriver.support import expected_conditions as EC

# 期待元素出現要透過什麼方式指定，通常與 EC、WebDriverWait 一起使用
from selenium.webdriver.common.by import By

# 強制等待 (執行期間休息一下)
from time import sleep

# 整理 json 使用的工具
import json

# 執行 command 的時候用的
import os

# 子處理程序，用來取代 os.system 的功能
import subprocess


# 啟動瀏覽器工具的選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")         #最大化視窗
my_options.add_argument("--incognito")               #開啟無痕模式
my_options.add_argument("--disable-popup-blocking") #禁用彈出攔截
my_options.add_argument("--disable-notifications")  #取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  #設定為正體中文

# 使用 Chrome 的 WebDriver
driver = webdriver.Chrome(
    options = my_options,
    service = Service(ChromeDriverManager().install())
)

driver.get('https://www.google.com.tw/maps/@25.0984315,121.5255009,16z')


def filterFunc():
    try:
        # 等待篩選元素出現
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[aria-label="餐廳"]')
            )
        )
        
        # 按下篩選元素，使項目浮現
        driver.find_element(By.CSS_SELECTOR, 
            'button[aria-label="餐廳"]'
        ).click()
        
        # 等待
        sleep(2)
        
    except TimeoutException:
        print('等候逾時!')

# 滾動頁面
def scroll():

    '''
    innerHeight => 瀏覽器內部的高度
    offset => 當前捲動的量(高度)
    count => 累計無效滾動次數
    limit => 最大無效滾動次數
    '''
    innerHeight = 0
    offset = 0
    count = 0
    limit = 3
    
    # 在捲動到沒有元素動態產生前，持續捲動
    while count <= limit:

        # focus到那個窗格
        focus = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')

        # 執行js指令捲動頁面，每次移動高度
        offset = driver.execute_script("return arguments[0].scrollTop = arguments[0].scrollHeight", focus)
     
        # 等待
        sleep(3)
        
        # 透過執行 js 語法來取得捲動後的當前總高度
        innerHeight = driver.execute_script("return arguments[0].scrollTop = arguments[0].scrollHeight", focus)

        # 經過計算，如果滾動距離(offset)大於等於視窗內部總高度(innerHeight)，代表已經到底了
        if offset == innerHeight:
            count += 1

        if count == limit:
            break    

def data():


if __name__ == '__main__':
    filterFunc()
    scroll()
    data()