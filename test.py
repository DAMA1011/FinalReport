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
from time import sleep

# 整理 json 使用的工具
import json

# 執行 command 的時候用的
import os

# 子處理程序，用來取代 os.system 的功能
import subprocess

# 匯入 regex 套件
import re

# 啟動瀏覽器工具的選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")  #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")  #最大化視窗
my_options.add_argument("--incognito")  #開啟無痕模式
my_options.add_argument("--disable-popup-blocking")  #禁用彈出攔截
my_options.add_argument("--disable-notifications")  #取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  #設定為正體中文

# 使用 Chrome 的 WebDriver
driver = webdriver.Chrome(
    options = my_options,
    service = Service(ChromeDriverManager().install())
)

# 開啟目標網頁
driver.get('https://www.google.com.tw/maps/@25.0636069,121.5124937,16.5z')

# 抵達目標網頁
def TargetMap():
    try:
        # 等待篩選元素出現
        # WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located(
        #         (By.CSS_SELECTOR, 'button[aria-label="搜尋"]')
        #     )
        # )
        
        sleep(4)

        ac = ActionChains(driver)
        # 輸入條件，按下 ENTER
        ac.send_keys('大同區 餐廳').send_keys(Keys.ENTER)
        ac.perform()

        sleep(2)

        # 找尋「地圖移動時更新結果」的標籤
        clickUpDate = driver.find_element(By.CSS_SELECTOR, 'button.D6NGZc')

        ac = ActionChains(driver)
        # 將「地圖移動時更新結果」打勾
        ac.click(clickUpDate)
        ac.perform()

        sleep(2)

        # 按下篩選元素，使項目浮現
        # driver.find_element(By.CSS_SELECTOR, 'button[aria-label="餐廳"]').click()
               
    except TimeoutException:
        print('等候逾時!')

# 滾動頁面
def Scroll():
    offset = 0
    innerHeight = 0
    count = 0  # 累計無效滾動次數
    limit = 2  # 最大無效滾動次數
      
    # 在捲動到沒有元素動態產生前，持續捲動
    while count <= limit:
        # focus: 主角頁面
        focus = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')

        # offset: 拉槓到頁面頂端的距離
        offset = driver.execute_script('return arguments[0].scrollTop', focus)
        # print(offset)

        # 執行js指令捲動頁面
        driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', focus)

        # innerHeight: 頁面高度 = 拉槓到頁面頂端的距離
        innerHeight = driver.execute_script('return arguments[0].scrollHeight = arguments[0].scrollTop', focus)
        # print(innerHeight)

        # 另一個方法，待研究
        # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", focus)

        sleep(1.5)

        # 經過計算，如果「拉槓到頁面頂端的距離」(offset)等於「頁面高度 = 拉槓到頁面頂端的距離」(innerHeight)，代表已經到底了
        if offset == innerHeight:
            count += 1

        # 計數器等於限制數則跳脫
        if count == limit:
            break    

    print("已到底，滾動結束")

def Data():
    nameList = []  # 存放首頁滾動完的所有店家資訊網址
    
    # 搜尋首頁滾動完的所有店家資訊網址
    for a in driver.find_elements(By.CSS_SELECTOR, 'div[data-js-log-root] div[role="article"] a[aria-label]'):
        nameList.append(a.get_attribute("href"))

    sleep(5)

    try:
        for i in range(len(nameList)):

            dataList = []  # 存放各個店家的目標資訊

            # 到訪所有店家資訊網址
            driver.get(nameList[i])

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'div[data-js-log-root][role="region"] div[data-js-log-root] button[data-item-id="oloc"] div[style^=font-family]')
                )
            )

            # 查詢是否符合士林區、大同區
            type = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root][role="region"] div[data-js-log-root] button[data-item-id="oloc"] div[style^=font-family]')
            regex = r'.*大同區.*'
            result = re.match(regex, type.get_attribute('innerText'))
            if result != None:
                # 店家名稱
                name = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] h1 span').get_attribute('innerText')
                print(name)

                # 評分星數
                star = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] span[aria-hidden="true"]').get_attribute('innerText')
                print(star)

                # 消費水平(先取消)
                # cost = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] span[jsan="0.aria-label"]').get_attribute('innerText')
                # print(cost)

                # 店家地址
                address = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] [role="region"] div[data-js-log-root] button[data-item-id="address"] div[style^=font-family]').get_attribute('innerText')
                print(address)

                # 營業時間
                time = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root][role="region"] div[data-js-log-root][style^=font-family] div[aria-label]').get_attribute('aria-label')
                print(time)

                # 店家官網
                net = driver.find_element(By.CSS_SELECTOR, 'div[role="region"] a[data-item-id="authority"][href]').get_attribute('href')
                print(net)

                # 店家電話
                phone = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button[aria-label^=電話號碼] div[style^=font-family]').get_attribute('innerText')
                print(phone)

                # 所在行政區
                post = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button[aria-label^=Plus] div[style^=font-family]').get_attribute('innerText')
                print(post)
                print('=' * 150)

                # dataList.append({
                #     'name': name,
                #     'star': star,
                #     'cost': cost,
                #     'address': address,
                #     'time': time,
                #     'net': net,
                #     'phone': phone,
                #     'post': post
                # })

            sleep(3)

        # 寫出 json 檔
        # with open('大同區 餐廳.json', 'w', encoding='utf-8') as file:
        #     file.write(json.dump(dataList, ensure_ascii=False, indent=4))
    except NoSuchElementException:
        print(None)
        pass

def test():
    dataList = []

    driver.get('https://www.google.com.tw/maps/place/Podium/data=!4m7!3m6!1s0x3442af0cd0c0dbdf:0x9cee3c4061bafb68!8m2!3d25.0953089!4d121.526626!16s%2Fg%2F11j47nbpdv!19sChIJ39vA0AyvQjQRaPu6YUA87pw?authuser=0&hl=zh-TW&rclk=1')

    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-js-log-root][role="region"] div[data-js-log-root] button[data-item-id="oloc"] div[style^=font-family]')
            )
        )

    # 查詢是否符合士林區、大同區
    type = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root][role="region"] div[data-js-log-root] button[data-item-id="oloc"] div[style^=font-family]')
    regex = r'.*士林區.*'
    result = re.match(regex, type.get_attribute('innerText'))
    if result != None:
        name = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] h1 span').get_attribute('innerText')
        print(name)

        star = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] span[aria-hidden="true"]').get_attribute('innerText')
        print(star)

        # cost = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] span[jsan="0.aria-label"]').get_attribute('innerText')
        # print(cost)

        address = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] [role="region"] div[data-js-log-root] button[data-item-id="address"] div[style^=font-family]').get_attribute('innerText')
        print(address)

        time = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root][role="region"] div[data-js-log-root][style^=font-family] div[aria-label]').get_attribute('aria-label')
        print(time)

        net = driver.find_element(By.CSS_SELECTOR, 'div[role="region"] a[data-item-id="authority"][href]').get_attribute('href')
        print(net)

        phone = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button[aria-label^=電話號碼] div[style^=font-family]').get_attribute('innerText')
        print(phone)

        post = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button[aria-label^=Plus] div[style^=font-family]').get_attribute('innerText')
        print(post)

        # dataList.append({
        #     'name': name,
        #     'star': star,
        #     'cost': cost,
        #     'address': address,
        #     'time': time,
        #     'net': net,
        #     'phone': phone,
        #     'post': post
        # })



if __name__ == '__main__':
    TargetMap()
    Scroll()
    # Data()
    # test()