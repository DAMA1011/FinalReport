import json, csv
import pandas as pd   

pf1 = pd.read_json('台北市景點.json')
pdf1 = (pf1['href']).tolist()[0]
# pf2 = pd.read_json('台北市士林區士東路.json')
# pdf2 = (pf2['href']).tolist()[0]
# pf3 = pd.read_json('台北市士林區中山北路七段.json')
# pdf3 = (pf3['href']).tolist()[0]
# pf4 = pd.read_json('台北市士林區中正路.json')
# pdf4 = (pf4['href']).tolist()[0]
# pf5 = pd.read_json('台北市士林區天母東路.json')
# pdf5 = (pf5['href']).tolist()[0]
# pf6 = pd.read_json('台北市士林區平菁街.json')
# pdf6 = (pf6['href']).tolist()[0]
# pf7 = pd.read_json('台北市士林區仰德大道三段.json')
# pdf7 = (pf7['href']).tolist()[0]
# pf8 = pd.read_json('台北市士林區竹子湖路.json')
# pdf8 = (pf8['href']).tolist()[0]
# pf9 = pd.read_json('台北市士林區至善路三段.json')
# pdf9 = (pf9['href']).tolist()[0]
# pf10 = pd.read_json('台北市士林區忠誠路二段.json')
# pdf10 = (pf10['href']).tolist()[0]
# pf11 = pd.read_json('台北市士林區承德路五段.json')
# pdf11 = (pf11['href']).tolist()[0]
# pf12 = pd.read_json('台北市士林區後港街.json')
# pdf12 = (pf12['href']).tolist()[0]
# pf13 = pd.read_json('台北市士林區格致路.json')
# pdf13 = (pf13['href']).tolist()[0]
# pf14 = pd.read_json('台北市士林區福國路.json')
# pdf14 = (pf14['href']).tolist()[0]
# pf15 = pd.read_json('台北市士林區劍南路.json')
# pdf15 = (pf15['href']).tolist()[0]

sum = 0
pdfsum = []

# for i in [pdf1, pdf2, pdf3, pdf4, pdf5, pdf6, pdf7, pdf8, pdf9, pdf10, pdf11, pdf12, pdf13, pdf14, pdf15]:    
#     pdfsum += i

# print(len(pdf1))
# print(type(pdf1))

# pdf1 = list(set(pdf1))
# print(len(pdf1))
# print(type(pdf1))

# # 先寫出 List 檔
# with open('台北市景點List.csv', 'w') as file:
#     write = csv.writer(file)
#     write.writerow(pdf1)

# # 再讀近來轉換符號，寫出 String 檔
# with open('台北市景點List.csv') as file:
#     string = file.read()

# result = string.replace(',', '\n')

# with open('台北市景點String.csv', 'w') as file:
#     file.write(result)