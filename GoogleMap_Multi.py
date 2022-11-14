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

# 讓顯示好讀
import pprint

# 平行任務處理
from concurrent.futures import ProcessPoolExecutor as ppe

googleMap = 'https://www.google.com.tw/maps?hl=zh-TW'

nameList = []  # 存放首頁查詢滾動完的所有店家資訊網址

dataList = []  # 存放各個店家的目標資訊

# 啟動瀏覽器
def browser():

    # 啟動瀏覽器的工具選項
    my_options = webdriver.ChromeOptions()
    # my_options.add_argument("--headless")  #不開啟實體瀏覽器背景執行
    # my_options.add_argument("--start-maximized")  #最大化視窗
    my_options.add_argument("--incognito")  #開啟無痕模式
    my_options.add_argument("--disable-popup-blocking")  #禁用彈出攔截
    my_options.add_argument("--disable-notifications")  #取消 chrome 推播通知
    my_options.add_argument("--lang=zh-TW")  #設定為正體中文
    my_options.add_experimental_option("detach", True)
    my_service = Service(ChromeDriverManager().install())

    # 使用 Chrome 的 WebDriver
    return webdriver.Chrome(options = my_options, service = my_service)

# 開啟目標網頁
def TargetMap(link: str):

    # 開啟 Google Map 首頁
    driver = browser()
    driver.get(googleMap)

    # 等待元素出現
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[aria-label="搜尋"]')
        )
    )
    
    sleep(2) # 依網路狀況調整

    ac = ActionChains(driver)
    # 輸入條件
    ac.send_keys(link)
    ac.pause(1)
    # 按下 ENTER
    ac.send_keys(Keys.ENTER)
    ac.perform()

    # 滾動頁面
    offset = 0
    innerHeight = 0
    count = 0  # 累計無效滾動次數
    limit = 2  # 最大無效滾動次數
      
    # 持續捲動
    while count <= limit:
        # 等待篩選元素出現
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[role="feed"]')
            )
        )

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

        sleep(3)  # 依網路狀況調整

        # 經過計算，如果「拉槓到頁面頂端的距離」(offset)等於「頁面高度 = 拉槓到頁面頂端的距離」(innerHeight)，代表已經到底了
        if offset == innerHeight:
            count += 1

        # 計數器等於限制數則跳脫
        if count == limit:
            break 
    
    try:
        # 檢查是否滾動到底，並且有顯示「你已看完所有搜尋結果」的標籤
        driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] div[data-js-log-root] div[data-js-log-root] p[style^="font-family"] span[style^="color"]')

        # 紀錄首頁滾動完的所有店家資訊網址
        for a in driver.find_elements(By.CSS_SELECTOR, 'div[data-js-log-root] div[role="article"] a[aria-label]'):
            nameList.append(a.get_attribute("href"))

        print(f'[{link}] 搜尋已到底，滾動結束，有 {len(nameList)} 筆店家')

        # with open('大同區大龍街餐廳.json', 'w', encoding='utf-8') as file:
        #     json.dump(nameList, file, ensure_ascii=False, indent=4)

        sleep(2)

        for i in range(len(nameList)):

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
                try:
                    # 店名
                    place_name = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] h1 span').get_attribute('innerText')
                except NoSuchElementException:
                    place_name = ""
                # print(place_name)
                try:
                    # 星數
                    total_rating_str = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] span[aria-hidden="true"]').get_attribute('innerText')
                    total_rating = float(total_rating_str)
                except NoSuchElementException:
                    total_rating = ""
                # print(total_rating)
                try:
                    # 地點標籤、類別
                    place_category = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] div[data-js-log-root] div[style^="font-family"] > span button[jsaction][jstcache][class][jsan]').get_attribute('innerText')
                except NoSuchElementException:
                    place_category = ""
                # print(place_category)
                try:
                    # 評論數
                    total_reviews_str = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] div[data-js-log-root] div[style^="font-family"] div[role="button"] span[style] span[aria-label][jstcache][jsan]').get_attribute('innerText')
                    total_reviews_cama = (total_reviews_str.split(' ')[0])
                    total_reviews = re.sub(',', '', total_reviews_cama)
                except NoSuchElementException:
                    total_reviews = ""
                # print(total_reviews)
                try:
                    # 消費水平
                    cost = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] span[aria-label^="價格"]').get_attribute('innerText')
                except NoSuchElementException:
                    cost = ""
                # print(cost)
                try:
                    # 地址
                    address = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] [role="region"] div[data-js-log-root] button[data-item-id="address"] div[style^=font-family]').get_attribute('innerText')
                except NoSuchElementException:
                    address = ""
                # print(address)
                try:
                    # 行政區
                    district_str = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button[aria-label^=Plus] div[style^=font-family]').get_attribute('innerText')
                    district = district_str.split(' ')[2] + ' ' + district_str.split(' ')[1]
                except NoSuchElementException:
                    district = ""
                # print(district)
                try:
                    # 提供內用(boolean)
                    driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button div[style^="font-family"] div[aria-label="提供內用"]')
                    eat_in = 1
                except NoSuchElementException:
                    eat_in = 0
                # print(eat_in)                  
                try:
                    # 提供外帶服務(boolean)
                    driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button div[style^="font-family"] div[aria-label="提供外帶服務"]')
                    to_go_1 = 1
                except NoSuchElementException:
                    to_go_1 = 0
                # print(to_go_1)      
                try:
                    # 提供路邊取餐服務(boolean)
                    driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button div[style^="font-family"] div[aria-label="提供路邊取餐服務"]')
                    to_go_2 = 1
                except NoSuchElementException:
                    to_go_2 = 0
                # print(to_go_2) 
                try:
                    # 提供外送服務(boolean)
                    driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button div[style^="font-family"] div[aria-label="提供外送服務"]')
                    delivery = 1
                except NoSuchElementException:
                    delivery = 0
                # print(delivery) 
                try:
                    # 營業時間
                    opening_hour = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root][role="region"] div[data-js-log-root][style^=font-family] div[aria-label]').get_attribute('aria-label')
                except NoSuchElementException:
                    opening_hour = ""
                # print(opening_hour)
                try:
                    # 景點店家官網
                    website = driver.find_element(By.CSS_SELECTOR, 'div[role="region"] a[data-item-id="authority"][href]').get_attribute('href')
                except NoSuchElementException:
                    website = ""
                # print(website)
                try:
                    # 景點店家電話
                    phone = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] button[aria-label^=電話號碼] div[style^=font-family]').get_attribute('innerText')
                except NoSuchElementException:
                    phone = ""
                # print(phone)
                try:
                    # 是否關閉
                    close = driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] div[data-js-log-root] div[style^="font-family"] span[style="color:#D93025"] span').get_attribute('innerText')
                except NoSuchElementException:
                    close = ""
                # print(close)
                    # 爬取地點資料當天的日期
                    t = time.time()
                    place_acquisition_date = time.ctime(t)

                # print('=' * 200)

                dataList.append({
                    'google_url': nameList[i],  # google maps網址
                    'place_name': place_name,  # 店名
                    'total_rating': total_rating,  # 星數
                    'place_category': place_category,  # 地點標籤、類別
                    'total_reviews': total_reviews,  # 評論數
                    'cost': cost,  # 消費水平
                    'address': address,  # 地址
                    'district': district,  # 行政區
                    'eat_in': eat_in,  # 提供內用(boolean)
                    'to_go_1': to_go_1,  # 提供外帶服務(boolean)
                    'to_go_2': to_go_2,  # 提供路邊取餐服務(boolean)
                    'delivery': delivery,  # 提供外送服務(boolean)
                    'opening_hour': opening_hour,  # 營業時間
                    'website': website,  # 景點店家官網
                    'phone': phone,  # 景點店家電話
                    'close': close,  # 是否關閉
                    'place_acquisition_date': place_acquisition_date  # 爬取地點資料當天的日期
                })

            sleep(0.5)

        # pprint.pprint(dataList)

        # 寫出 json 檔
        with open(f'{link}.json', 'w', encoding='utf-8') as file:
            (json.dump(dataList, file, ensure_ascii=False, indent=4))

        sleep(1)

    except NoSuchElementException:
        driver.quit()
        TargetMap()

# 平行處理
def FirstPage():
    links = ['大同區天水路餐廳', '大同區安西街餐廳']

    with ppe(max_workers=2) as executor:        
        executor.map(TargetMap, links)       

if __name__ == '__main__':
    time1 = time.time()
    FirstPage()  
    print(f'執行總花費時間: {time.time() - time1}')


# links = ['大同區大龍街餐廳', '大同區五原路餐廳', '大同區天水路餐廳', '大同區太原路餐廳', '大同區市民大道一段餐廳', '大同區平陽街餐廳', '大同區民生西路餐廳', '大同區民族西路餐廳', '大同區民樂街餐廳', '大同區民權西路餐廳', '大同區永昌街餐廳', '大同區甘州街餐廳', '大同區甘谷街餐廳', '大同區伊寧街餐廳', '大同區安西街餐廳', '大同區西寧北路餐廳', '大同區赤峰街餐廳', '大同區延平北路一段餐廳', '大同區延平北路二段餐廳', '大同區延平北路三段餐廳', '大同區延平北路四段餐廳', '大同區忠孝西路二段餐廳', '大同區承德路一段餐廳', '大同區承德路二段餐廳', '大同區承德路三段餐廳', '大同區昌吉街餐廳', '大同區長安西路餐廳', '大同區保安街餐廳', '大同區南京西路餐廳', '大同區哈密街餐廳', '大同區迪化街一段餐廳', '大同區迪化街二段餐廳', '大同區重慶北路一段餐廳', '大同區重慶北路二段餐廳', '大同區重慶北路三段餐廳', '大同區庫倫街餐廳', '大同區酒泉街餐廳', '大同區涼州街餐廳', '大同區通河西街一段餐廳', '大同區敦煌路餐廳', '大同區景化街餐廳', '大同區華亭街餐廳', '大同區華陰街餐廳', '大同區貴德街餐廳', '大同區塔城街餐廳', '大同區萬全街餐廳', '大同區寧夏路餐廳', '大同區撫順街餐廳', '大同區鄭州路餐廳', '大同區興城街餐廳', '大同區錦西街餐廳', '大同區環河北路一段餐廳', '大同區環河北路二段餐廳', '大同區歸綏街餐廳', '大同區雙連街餐廳', '大同區蘭州街餐廳']