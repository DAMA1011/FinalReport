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

# 整理 json 使用的工具
import json

# 讓顯示好讀
import pprint

# 平行任務處理
from concurrent.futures import ProcessPoolExecutor as ppe
from concurrent.futures import as_completed

# 啟動瀏覽器
def browser():

    # 啟動瀏覽器的工具選項
    my_options = webdriver.ChromeOptions()
    # my_options.add_argument("--headless")  #不開啟實體瀏覽器背景執行
    # my_options.add_argument("--start-maximized")  #最大化視窗
    # my_options.add_argument('window-size=1920,1080')
    my_options.add_argument("--incognito")  #開啟無痕模式
    my_options.add_argument("--disable-popup-blocking")  #禁用彈出攔截
    my_options.add_argument("--disable-notifications")  #取消 chrome 推播通知
    my_options.add_argument("--lang=zh-TW")  #設定為正體中文
    my_options.add_argument('--disable-gpu')  # google document 提到需要加上這個屬性來規避 bug
    my_options.add_experimental_option("detach", True)
    my_options.add_experimental_option('excludeSwitches', ['enable-logging'])
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
    # 輸入 Keyword
    ac.send_keys(links)
    ac.pause(1)
    # 按下 ENTER
    ac.send_keys(Keys.ENTER)
    ac.perform()

    sleep(4) # 依網路狀況調整

    urlList = []  # 存放首頁查詢滾 動完的所有店家資訊網址

    # 滾動頁面
    offset = 0
    innerHeight = 0
    count = 0  # 累計無效滾動次數
    limit = 2  # 最大無效滾動次數
    done = True
    refresh_counter = 0 

    try:

        # # 等待篩選元素出現
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.CSS_SELECTOR, 'div[role="feed"]')
        #     )
        # )

        # focus: 主角頁面
        focus = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
        pass

        # 持續捲動
        while done:

            try:

                # focus: 主角頁面
                focus = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')

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

                    count = 0  # 計數器歸零

                    refresh_counter += 1

                    if refresh_counter == 3:

                        print(f'[{links}] 重新整理三次，直接抓取網址')

                        break

                    driver.refresh()  # 重整頁面
            
        # 紀錄首頁滾動完的所有店家資訊網址
        for a in driver.find_elements(By.CSS_SELECTOR, 'div[data-js-log-root] div[role="article"] > a[aria-label]'):
            urlList.append(a.get_attribute("href"))

        print(f'[{links}] 搜尋已到底，滾動結束，有 {len(urlList)} 筆店家')

        sleep(2)

        driver.quit()
        
        # pprint.pprint(urlList)
        # print(len(urlList))

        return urlList

    except NoSuchElementException:

        print(f'[{links}] 掛掉了!!!!!')

        driver.quit()

        return []

# 平行處理
def FirstPage():

    comList = []  # 整合所有 Keywords 查詢完的網頁 List
    allurlList = []  # 最終寫出檔案的 List
    keywords = []  # 儲存所有條件字的組合

    street = ['赤峰街']

    category = ['火鍋', '拉麵', '日本料理', '美式', '義式', '法式', '中式', '台灣菜', '韓式', '德式', '地中海料理', '印度料理', '越式', '港式', '泰式', '南洋', '素食', '鐵板燒', '餐酒館', '咖啡廳', '熱炒店', '早午餐', '甜點店', '燒肉', '海鮮餐廳', '牛排']

    for item_1 in street:
        for item_2 in category:
            links = f'大同區{item_1}{item_2}'

            keywords.append(links) 

    with ppe(max_workers=10) as executor:     
        results = [executor.submit(TargetMap, key) for key in keywords]
        try:
            for result in as_completed(results):
                comList += (result.result())
        except TimeoutException:
            pass

    allurlList.append({
        "herf": (list(set(comList)))  # 篩選掉重複的網址
    })

    # # pprint.pprint(allurlList)
    # print(len(list(set(comList))))

    # 寫出 json 檔
    with open(f'台北市大同區1.json', 'w', encoding='utf-8') as file:
        (json.dump(allurlList, file, ensure_ascii=False, indent=4))
    
    sleep(3)

    print(len(list(set(comList))))

if __name__ == '__main__':
    time1 = time.time()
    FirstPage()
    print(f'執行總花費時間: {time.time() - time1}')


# ['大龍街_', '五原路_', '天水路_', '太原路_', '市民大道一段_', '平陽街_', '民生西路_', '民族西路_', '民樂街_', '民權西路_', '永昌街_', '甘州街_', '甘谷街_', '伊寧街_', '安西街_', '西寧北路_', '赤峰街', '延平北路一段', '延平北路二段', '延平北路三段', '延平北路四段', '忠孝西路二段', '承德路一段', '承德路二段', '承德路三段', '昌吉街', '長安西路', '保安街', '大南京西路', '哈密街', '迪化街一段', '迪化街二段', '重慶北路一段', '重慶北路二段', '重慶北路三段', '庫倫街', '酒泉街', '涼州街', '通河西街一段', '敦煌路', '景化街', '華亭街', '華陰街', '貴德街', '塔城街', '萬全街', '寧夏路', '撫順街', '鄭州路', '興城街', '錦西街', '環河北路一段', '環河北路二段', '歸綏街', '雙連街_', '蘭州街_']

# ['火鍋', '拉麵', '日本料理', '美式', '義式', '法式', '中式', '台灣菜', '韓式', '德式', '地中海料理', '印度料理', '越式', '港式', '泰式', '南洋', '素食', '鐵板燒', '餐酒館', '咖啡廳', '熱炒店', '早午餐', '甜點店', '燒肉', '海鮮餐廳', '牛排'] # 26 * category

# ["下樹林街", "中山北路四段", "中山北路五段", "中山北路六段", "中山北路七段", "中庸一路", "中庸二路", "中庸五路", "中正路", "中社路一段", "中社路二段", "中興街", "中華路", "仁民路", "仰德大道一段", "仰德大道二段", "仰德大道三段", "仰德大道四段", "倫等街", "光華路", "克強路", "凱旋路", "前港街", "前街", "劍南路", "劍潭路", "力行街", "和平路", "和豐街", "國泰街", "基河路", "士商路", "士東路", "大亨路", "大光街", "大北路", "大南路", "大東路", "大西路", "天母北路", "天母東路", "天母西路", "天玉街", "安平街", "小北街", "小南街", "小東街", "小西街", "平菁街", "幸福街", "延平北路五段", "延平北路六段", "延平北路七段", "延平北路八段", "延平北路九段", "建業路", "後港街", "後街", "德行東路", "德行西路", "志成街", "忠勇街", "忠義街", "忠誠路一段", "忠誠路二段", "愛富一街", "愛富三街", "愛富三街長生巷", "愛富二街", "愛富二街厚生巷", "愛富二街樂生巷", "承德路四段", "承德路五段", "故宮路", "文昌路", "文林路", "新園街", "新安路", "明溪街", "東山路", "格致路", "永公路", "永平街", "環河北路三段", "磺溪街", "社中街", "社子街", "社正路", "福國路", "福壽街", "福德路", "福志路", "福林路", "福榮街", "福港街", "福華路", "竹子湖路", "美崙街", "美德街", "翠山街", "臨溪路", "自祥街", "至善路一段", "至善路二段", "至善路三段", "至誠路一段", "至誠路二段", "芝玉路一段", "芝玉路二段", "莊頂路", "菁山路", "華光街", "華岡路", "華榮街", "華聲街", "華興街", "華齡街", "葫東街", "葫蘆街", "貴富街", "通河東街一段", "通河東街二段", "通河街", "通河西街一段", "通河西街二段", "重慶北路四段", "長春街", "陽明路一段", "陽明路二段", "雙溪街", "雨聲街", "雨農路"]
