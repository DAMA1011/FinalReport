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
    my_options.add_argument('--disable-gpu')  # google document 提到需要加上這個屬性來規避 bug
    my_options.add_experimental_option("detach", True)
    my_service = Service(ChromeDriverManager().install())

    # 使用 Chrome 的 WebDriver
    return webdriver.Chrome(options = my_options, service = my_service)


# 開啟目標網頁
def TargetMap(links: str):

    googleMap = 'https://www.google.com.tw/maps?hl=zh-TW'

    # 開啟 Google Map 首頁
    driver = browser()
    driver.get(googleMap)

    # 等待元素出現
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[aria-label="搜尋"]')
        )
    )
    
    sleep(1) # 依網路狀況調整

    ac = ActionChains(driver)
    # 輸入條件
    ac.send_keys(links)
    ac.pause(1)
    # 按下 ENTER
    ac.send_keys(Keys.ENTER)
    ac.perform()

    urlList = []  # 存放首頁查詢滾 動完的所有店家資訊網址

    # 滾動頁面
    offset = 0
    innerHeight = 0
    count = 0  # 累計無效滾動次數
    limit = 2  # 最大無效滾動次數
    done = True 

    # 等待篩選元素出現
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[role="feed"]')
        )
    )

    # focus: 主角頁面
    focus = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')

    # 持續捲動
    while done:

        try:
            
            # 檢查是否滾動到底，並且有顯示「你已看完所有搜尋結果」的標籤
            driver.find_element(By.CSS_SELECTOR, 'div[data-js-log-root] div[data-js-log-root] div[data-js-log-root] p[style^="font-family"] span[style^="color"]')

            break
            
        except NoSuchElementException:

            # offset: 拉槓到頁面頂端的距離
            offset = driver.execute_script('return arguments[0].scrollTop', focus)
            # print(offset)

            # 執行js指令捲動頁面
            driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', focus)

            # innerHeight: 頁面高度 = 拉槓到頁面頂端的距離
            innerHeight = driver.execute_script('return arguments[0].scrollHeight = arguments[0].scrollTop', focus)
            # print(innerHeight)

            sleep(2)  # 依網路狀況調整

            # 經過計算，如果「拉槓到頁面頂端的距離」(offset)等於「頁面高度 = 拉槓到頁面頂端的距離」(innerHeight)，代表已經到底了
            if offset == innerHeight:
                count += 1

            # 計數器等於限制數則跳脫
            if count == limit:

                print(f'[{links}] 捲動失敗! 重新整理!')

                driver.refresh()

            
             
    # 紀錄首頁滾動完的所有店家資訊網址
    for a in driver.find_elements(By.CSS_SELECTOR, 'div[data-js-log-root] div[role="article"] a[aria-label]'):
        urlList.append(a.get_attribute("href"))

    print(f'[{links}] 搜尋已到底，滾動結束，有 {len(urlList)} 筆店家')

    sleep(2)

    driver.quit()

          
    # print(urlList)

    return urlList

# 平行處理
def FirstPage():
    links = ['大同區大龍街餐廳', '大同區五原路餐廳', '大同區天水路餐廳']

    allurlList = []
    with ppe(max_workers=3) as executor:     
        for results in executor.map(TargetMap, links):
            return results

    # allurlList.append({
    #     "herf": list(set(results))
    # })

    # pprint.pprint(allurlList)
          


def writeout(results: list):

    allurlList = []

    allurlList.append({
        "herf": list(set(results))
    })

    pprint.pprint(allurlList)

    # # 寫出 json 檔
    # with open(f'大同區餐廳網址.json', 'w', encoding='utf-8') as file:
    #     (json.dump(allurlList, file, ensure_ascii=False, indent=4))



if __name__ == '__main__':
    time1 = time.time()
    FirstPage()
    # writeout(FirstPage()) 
    print(f'執行總花費時間: {time.time() - time1}')


# links = ['大同區大龍街餐廳', '大同區五原路餐廳', '大同區天水路餐廳', '大同區太原路餐廳', '大同區市民大道一段餐廳', '大同區平陽街餐廳', '大同區民生西路餐廳', '大同區民族西路餐廳', '大同區民樂街餐廳', '大同區民權西路餐廳', '大同區永昌街餐廳', '大同區甘州街餐廳', '大同區甘谷街餐廳', '大同區伊寧街餐廳', '大同區安西街餐廳', '大同區西寧北路餐廳', '大同區赤峰街餐廳', '大同區延平北路一段餐廳', '大同區延平北路二段餐廳', '大同區延平北路三段餐廳', '大同區延平北路四段餐廳', '大同區忠孝西路二段餐廳', '大同區承德路一段餐廳', '大同區承德路二段餐廳', '大同區承德路三段餐廳', '大同區昌吉街餐廳', '大同區長安西路餐廳', '大同區保安街餐廳', '大同區南京西路餐廳', '大同區哈密街餐廳', '大同區迪化街一段餐廳', '大同區迪化街二段餐廳', '大同區重慶北路一段餐廳', '大同區重慶北路二段餐廳', '大同區重慶北路三段餐廳', '大同區庫倫街餐廳', '大同區酒泉街餐廳', '大同區涼州街餐廳', '大同區通河西街一段餐廳', '大同區敦煌路餐廳', '大同區景化街餐廳', '大同區華亭街餐廳', '大同區華陰街餐廳', '大同區貴德街餐廳', '大同區塔城街餐廳', '大同區萬全街餐廳', '大同區寧夏路餐廳', '大同區撫順街餐廳', '大同區鄭州路餐廳', '大同區興城街餐廳', '大同區錦西街餐廳', '大同區環河北路一段餐廳', '大同區環河北路二段餐廳', '大同區歸綏街餐廳', '大同區雙連街餐廳', '大同區蘭州街餐廳']