import json, csv
import pandas as pd   

pf1 = pd.read_json('台北市.json')
pdf1 = (pf1['href']).tolist()[0]
pf2 = pd.read_json('台北市.json')
pdf2 = (pf2['href']).tolist()[0]
pf3 = pd.read_json('台北市.json')
pdf3 = (pf3['href']).tolist()[0]
pf4 = pd.read_json('台北市.json')
pdf4 = (pf4['href']).tolist()[0]
pf5 = pd.read_json('台北市.json')
pdf5 = (pf5['href']).tolist()[0]
pf6 = pd.read_json('台北市.json')
pdf6 = (pf6['href']).tolist()[0]
pf7 = pd.read_json('台北市.json')
pdf7 = (pf7['href']).tolist()[0]
pf8 = pd.read_json('台北市.json')
pdf8 = (pf8['href']).tolist()[0]
pf9 = pd.read_json('台北市.json')
pdf9 = (pf9['href']).tolist()[0]
pf10 = pd.read_json('台北市.json')
pdf10 = (pf10['href']).tolist()[0]
pf11 = pd.read_json('台北市.json')
pdf11 = (pf11['href']).tolist()[0]
pf12 = pd.read_json('台北市.json')
pdf12 = (pf12['href']).tolist()[0]
pf13 = pd.read_json('台北市.json')
pdf13 = (pf13['href']).tolist()[0]
pf14 = pd.read_json('台北市.json')
pdf14 = (pf14['href']).tolist()[0]
pf15 = pd.read_json('台北市.json')
pdf15 = (pf15['href']).tolist()[0]
pf16 = pd.read_json('台北市.json')
pdf16 = (pf16['href']).tolist()[0]
pf17 = pd.read_json('台北市.json')
pdf17 = (pf17['href']).tolist()[0]
pf18 = pd.read_json('台北市.json')
pdf18 = (pf18['href']).tolist()[0]
pf19 = pd.read_json('台北市.json')
pdf19 = (pf19['href']).tolist()[0]
pf20 = pd.read_json('台北市.json')
pdf20 = (pf20['href']).tolist()[0]
pf21 = pd.read_json('台北市.json')
pdf21 = (pf21['href']).tolist()[0]
pf22 = pd.read_json('台北市.json')
pdf22 = (pf22['href']).tolist()[0]
pf23 = pd.read_json('台北市.json')
pdf23 = (pf23['href']).tolist()[0]
pf24 = pd.read_json('台北市.json')
pdf24 = (pf24['href']).tolist()[0]
pf25 = pd.read_json('台北市.json')
pdf25 = (pf25['href']).tolist()[0]

sum = 0
pdfsum = []

for i in [pdf1, pdf2, pdf3, pdf4, pdf5, pdf6, pdf7, pdf8, pdf9, pdf10, pdf11, pdf12, pdf13, pdf14, pdf15, pdf16, pdf17, pdf18, pdf19, pdf20, pdf21, pdf22, pdf23, pdf24, pdf25]:    
    pdfsum += i

# print(len(pdfsum))
# print(type(pdfsum))

# listsum = list(set(pdfsum))
# print(len(listsum))
# print(type(listsum))

# 先寫出 List 檔
# with open('大同區List.csv', 'w') as file:
#     write = csv.writer(file)
#     write.writerow(listsum)

# 再讀近來轉換符號，寫出 String 檔
# with open('大同區List.csv') as file:
#     string = file.read()

# result = string.replace(',', '\n')

# with open('大同區String.csv', 'w') as file:
#     file.write(result)