import pandas as pd
import re
import random
import folium
from folium import plugins
from flask import Flask, render_template
from db import get_conn, query_data, inser_or_update__data
import pymysql


con = pymysql.connect(host='127.0.0.1', user='root', password='Passw0rd!', database='project', charset='utf8') # 連線
df_r = pd.read_sql('select * from restaurant;', con=con) 
con.close()

# df_r = read_table(cur, "select * from restaurant")

# df_a = read_table(cur, "select * from spot")

print(df_r['monday'][1])
print(df_r.shape)
print(type(df_r['monday'][1]))
# print(df_a)
# print(df_a.shape)
# print(type(df_a))

# df_a = pd.read_csv('attraction_info_final_0106.csv')
# df_p = pd.read_csv('place_info_final_0103.csv')

# print(df_a.shape)
# print(df_p.shape)

# dl_p = df_p['google_url'].tolist()

# url_p = []
# for i in dl_p:
#     regex = r'1s0x.*:\w*'
#     match = re.findall(regex, i)
#     url_p.append(match)

# print(df_p.shape)
# print(len(dl_p))
# print(len(url_p))

# df2_p = pd.DataFrame(url_p, columns=['url'])

# print(df2_p.shape)

# df3_p = pd.concat([df_p, df2_p], axis=1)

# print(df3_p.shape)

# df3_p.to_csv('place_info_final_0103_url.csv', encoding='utf-8', index=False, sep=',')

# # ---------------------------------------------------------------------------------- #

# df_p = pd.read_csv('attraction_info_final_0106_origin.csv')

# df_p = df_p.drop(['place_category','cost','district','eat_in','to_go_1','to_go_2','delivery','opening_hours','website','close','place_acquisition_date','new_rating','new_review'],axis=1)

# df_p.to_csv('attraction_info_final_0106.csv', encoding='utf-8', index=False, sep=',')

# # ---------------------------------------------------------------------------------- #

# df_a = pd.read_csv('attraction_info_final_1217.csv')

# dl_a = df_a['google_url'].tolist()

# url_a = []
# for i in dl_a:
#     regex = r'1s0x.*:\w*'
#     match = re.findall(regex, i)
#     url_a.append(match)

# print(df_a.shape)
# print(len(dl_a))
# print(len(url_a))

# df2_a = pd.DataFrame(url_a, columns=['url'])

# print(df2_a.shape)

# df3_a = pd.concat([df_a, df2_a], axis=1)

# print(df3_a.shape)

# df3_a.to_csv('attraction_info_final_1217_url.csv', encoding='utf-8', index=False, sep=',')

# # ---------------------------------------------------------------------------------- #

# df_r = pd.read_csv('place_info_final_0103_url.csv')
# df_a = pd.read_csv('attraction_info_final_1217_url.csv')

# df_a_nightview = df_a[df_a['new_place_category'] == '夜景']
# df_a_nightmarket = df_a[df_a['new_place_category'] == '夜市']
# df_a2 = df_a.drop(df_a_nightview.index)
# df_a2 = df_a.drop(df_a_nightmarket.index)

# district = ["1", "2", "3", "4", "5"]

# weights = [0.15, 0.1, 0.15, 0.35, 0.25]

# selected_district = random.choices(district, weights=weights)[0]

# df = pd.DataFrame()

# df_a2 = df_a2[df_a2['district_num'] == int(selected_district)]

# df_a2['rating2'] = df_a2['total_rating'].apply(lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
# df_a2['weights'] = df_a2['rating2'] / df_a2['rating2'].sum()

# attraction_1 = df_a2.sample(n=1, weights=df_a2['weights'])

# df_a2 = df_a2.drop(attraction_1.index)

# attraction_2 = df_a2.sample(n=1, weights=df_a2['weights'])

# d_latitude = (attraction_1['latitude'].values -
#                   attraction_2['latitude'].values)[0]
# d_longitude = (attraction_1['longitude'].values -
#                 attraction_2['longitude'].values)[0]

# if abs(d_latitude) > abs(d_longitude):
#     # 緯度差距大於精度差距，以緯度分割
#     if d_latitude > 0:
#         # 如果attraction_1在attraction_2的上面

#         # 早餐店要篩選latitude > attraction_1的latitude
#         filt_r_1 = (df_r['new_place_category'] == '早午餐') & (
#             df_r['latitude'] > attraction_1['latitude'].values[0]) & (df_r['district_num'] == int(selected_district))
#         df_r_1 = df_r[filt_r_1]
#         if df_r_1.shape[0] != 0:
#             df_r_1['rating2'] = df_r_1['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_1['weights'] = df_r_1['rating2'] / df_r_1['rating2'].sum()
#             restaurant_1 = df_r_1.sample(n=1, weights=df_r_1['weights'])
#         else:
#             filt_r_1 = df_r['district_num'] == int(selected_district)
#             df_r_1 = df_r[filt_r_1]
#             df_r_1['rating2'] = df_r_1['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_1['weights'] = df_r_1['rating2'] / df_r_1['rating2'].sum()
#             restaurant_1 = df_r_1.sample(n=1, weights=df_r_1['weights'])

#         # category_list 接收回傳值
#         category_list = ['中式', '韓式', '台灣小吃/熱炒店', '異國料理',
#                         '港式', '意式', '燒烤店', '南洋', '美式', '火鍋', '素食']
#         if '咖啡甜點' in category_list:
#             category_list_new = category_list.copy()
#             category_list_new.remove('咖啡甜點')
#         else:
#             category_list_new = category_list.copy()
#         category_all = ['中式', '韓式', '台灣小吃/熱炒店', '異國料理',
#                         '港式', '意式', '燒烤店', '南洋', '美式', '火鍋', '素食']

#         # 午餐要選在attraction_1['latitude'] attraction_2['latitude']中間，且符合使用者選擇的類別
#         filt_r_2 = df_r[df_r['new_place_category'].isin(category_list_new)]
#         filt_r_2 = filt_r_2[attraction_1['latitude'].values[0]
#                             > filt_r_2['latitude']]
#         filt_r_2 = filt_r_2[attraction_2['latitude'].values[0]
#                             < filt_r_2['latitude']]
#         df_r_2 = filt_r_2[filt_r_2['district_num']
#                             == int(selected_district)]
#         df_r_2.shape[0]

#         if df_r_2.shape[0] != 0:
#             # 如果有在中間
#             df_r_2['rating2'] = df_r_2['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_2['weights'] = df_r_2['rating2'] / df_r_1['rating2'].sum()
#             restaurant_2 = df_r_2.sample(n=1, weights=df_r_2['weights'])
#         else:
#             # 如果不符合上述任一條件，就在該區隨機挑選一間餐廳
#             filt_r_2 = df_r[df_r['new_place_category'].isin(
#                 category_list_new)]
#             df_r_2 = filt_r_2[filt_r_2['district_num']
#                                 == int(selected_district)]
#             df_r_2['rating2'] = df_r_2['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_2['weights'] = df_r_2['rating2'] / df_r_1['rating2'].sum()
#             restaurant_2 = df_r_2.sample(n=1, weights=df_r_2['weights'])

#         # 景點3要篩選latitude < attraction_2的latitude
#         if '咖啡甜點' in category_list:

#             filt_r_3 = (df_r['latitude'] < attraction_2['latitude'].values[0]) & (
#                 df_r['district_num'] == int(selected_district)) & (df_r['new_place_category'] == '咖啡甜點')
#             df_r_3 = df_r[filt_r_3]
#             if df_r_3.shape[0] != 0:
#                 df_r_3['rating2'] = df_r_3['total_rating'].apply(
#                     lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                 df_r_3['weights'] = df_r_3['rating2'] / \
#                     df_r_3['rating2'].sum()
#                 restaurant_attraction_3 = df_r_3.sample(
#                     n=1, weights=df_r_3['weights'])
#             else:
#                 filt_a_3 = (df_a2['latitude'] < attraction_2['latitude'].values[0]) & (
#                     df_a2['district_num'] == int(selected_district))
#                 df_a_3 = df_a2[filt_a_3]
#                 if df_a_3.shape[0] != 0:
#                     df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                         lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                     df_a_3['weights'] = df_a_3['rating2'] / \
#                         df_a_3['rating2'].sum()
#                     restaurant_attraction_3 = df_a_3.sample(
#                         n=1, weights=df_a_3['weights'])
#                 else:
#                     # 如果不符合上述任一條件，就在該區隨機挑選一個景點
#                     filt_a_3 = df_a2['district_num'] == int(
#                         selected_district)
#                     df_a_3 = df_a2[filt_a_3]
#                     df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                         lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                     df_a_3['weights'] = df_a_3['rating2'] / \
#                         df_a_3['rating2'].sum()
#                     restaurant_attraction_3 = df_a_3.sample(
#                         n=1, weights=df_a_3['weights'])

#         else:
#             filt_a_3 = (df_a2['latitude'] < attraction_2['latitude'].values[0]) & (
#                 df_a2['district_num'] == int(selected_district))
#             df_a_3 = df_a2[filt_a_3]

#             if df_a_3.shape[0] != 0:
#                 df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                     lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                 df_a_3['weights'] = df_a_3['rating2'] / \
#                     df_a_3['rating2'].sum()
#                 restaurant_attraction_3 = df_a_3.sample(
#                     n=1, weights=df_a_3['weights'])
#             else:
#                 # 如果不符合上述任一條件，就在該區隨機挑選一個景點
#                 filt_a_3 = df_a2['district_num'] == int(selected_district)
#                 df_a_3 = df_a2[filt_a_3]
#                 df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                     lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                 df_a_3['weights'] = df_a_3['rating2'] / \
#                     df_a_3['rating2'].sum()
#                 restaurant_attraction_3 = df_a_3.sample(
#                     n=1, weights=df_a_3['weights'])

# #         filt_a_3 = (df_a2['latitude'] < attraction_2['latitude'].values[0]) & (df_a2['district_num'] == int(selected_district))
# #         df_a_3 = df_a2[filt_a_3]

# #         if df_a_3.shape[0] != 0:
# #             df_a_3['rating2'] = df_a_3['total_rating'].apply(lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
# #             df_a_3['weights'] = df_a_3['rating2'] / df_a_3['rating2'].sum()
# #             attraction_3 = df_a_3.sample(n=1, weights=df_a_3['weights'])
# #         else:
# #             # 如果不符合上述任一條件，就在該區隨機挑選一個景點
# #             filt_a_3 = df_a2['district_num'] == int(selected_district)
# #             df_a_3 = df_a2[filt_a_3]
# #             df_a_3['rating2'] = df_a_3['total_rating'].apply(lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
# #             df_a_3['weights'] = df_a_3['rating2'] / df_a_3['rating2'].sum()
# #             attraction_3 = df_a_3.sample(n=1, weights=df_a_3['weights'])

#     else:
#         # 如果attraction_1在attraction_2的下面
#         # 早餐店要篩選latitude < attraction_1的latitude
#         filt_r_1 = (df_r['new_place_category'] == '早午餐') & (
#             df_r['latitude'] < attraction_1['latitude'].values[0]) & (df_r['district_num'] == int(selected_district))
#         df_r_1 = df_r[filt_r_1]
#         if df_r_1.shape[0] != 0:
#             df_r_1['rating2'] = df_r_1['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_1['weights'] = df_r_1['rating2'] / df_r_1['rating2'].sum()
#             restaurant_1 = df_r_1.sample(n=1, weights=df_r_1['weights'])
#         else:
#             filt_r_1 = df_r['district_num'] == int(selected_district)
#             df_r_1 = df_r[filt_r_1]
#             df_r_1['rating2'] = df_r_1['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_1['weights'] = df_r_1['rating2'] / df_r_1['rating2'].sum()
#             restaurant_1 = df_r_1.sample(n=1, weights=df_r_1['weights'])

#         # category_list 接收回傳值
#         category_list = ['中式', '韓式', '台灣小吃/熱炒店', '異國料理',
#                         '港式', '意式', '燒烤店', '南洋', '美式', '火鍋', '素食']
#         if '咖啡甜點' in category_list:
#             category_list_new = category_list.copy()
#             category_list_new.remove('咖啡甜點')
#         else:
#             category_list_new = category_list.copy()
#         category_all = ['中式', '韓式', '台灣小吃/熱炒店', '異國料理',
#                         '港式', '意式', '燒烤店', '南洋', '美式', '火鍋', '素食']

#         # 午餐要選在attraction_1['latitude'] attraction_2['latitude']中間，且符合使用者選擇的類別
#         filt_r_2 = df_r[df_r['new_place_category'].isin(category_list_new)]
#         filt_r_2 = filt_r_2[attraction_1['latitude'].values[0]
#                             < filt_r_2['latitude']]
#         filt_r_2 = filt_r_2[attraction_2['latitude'].values[0]
#                             > filt_r_2['latitude']]
#         df_r_2 = filt_r_2[filt_r_2['district_num']
#                             == int(selected_district)]
#         df_r_2.shape[0]

#         if df_r_2.shape[0] != 0:
#             # 如果有在中間
#             df_r_2['rating2'] = df_r_2['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_2['weights'] = df_r_2['rating2'] / df_r_1['rating2'].sum()
#             restaurant_2 = df_r_2.sample(n=1, weights=df_r_2['weights'])
#         else:
#             # 如果不符合上述任一條件，就在該區隨機挑選一間餐廳
#             filt_r_2 = df_r[df_r['new_place_category'].isin(
#                 category_list_new)]
#             df_r_2 = filt_r_2[filt_r_2['district_num']
#                                 == int(selected_district)]
#             df_r_2['rating2'] = df_r_2['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_2['weights'] = df_r_2['rating2'] / df_r_1['rating2'].sum()
#             restaurant_2 = df_r_2.sample(n=1, weights=df_r_2['weights'])

#         # 景點3要篩選latitude > attraction_2的latitude
#         if '咖啡甜點' in category_list:

#             filt_r_3 = (df_r['latitude'] > attraction_2['latitude'].values[0]) & (
#                 df_r['district_num'] == int(selected_district)) & (df_r['new_place_category'] == '咖啡甜點')
#             df_r_3 = df_r[filt_r_3]
#             if df_r_3.shape[0] != 0:
#                 df_r_3['rating2'] = df_r_3['total_rating'].apply(
#                     lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                 df_r_3['weights'] = df_r_3['rating2'] / \
#                     df_r_3['rating2'].sum()
#                 restaurant_attraction_3 = df_r_3.sample(
#                     n=1, weights=df_r_3['weights'])
#             else:
#                 filt_a_3 = (df_a2['latitude'] < attraction_2['latitude'].values[0]) & (
#                     df_a2['district_num'] == int(selected_district))
#                 df_a_3 = df_a2[filt_a_3]
#                 if df_a_3.shape[0] != 0:
#                     df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                         lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                     df_a_3['weights'] = df_a_3['rating2'] / \
#                         df_a_3['rating2'].sum()
#                     restaurant_attraction_3 = df_a_3.sample(
#                         n=1, weights=df_a_3['weights'])
#                 else:
#                     # 如果不符合上述任一條件，就在該區隨機挑選一個景點
#                     filt_a_3 = df_a2['district_num'] == int(
#                         selected_district)
#                     df_a_3 = df_a2[filt_a_3]
#                     df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                         lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                     df_a_3['weights'] = df_a_3['rating2'] / \
#                         df_a_3['rating2'].sum()
#                     restaurant_attraction_3 = df_a_3.sample(
#                         n=1, weights=df_a_3['weights'])

#         else:
#             filt_a_3 = (df_a2['latitude'] > attraction_2['latitude'].values[0]) & (
#                 df_a2['district_num'] == int(selected_district))
#             df_a_3 = df_a2[filt_a_3]

#             if df_a_3.shape[0] != 0:
#                 df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                     lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                 df_a_3['weights'] = df_a_3['rating2'] / \
#                     df_a_3['rating2'].sum()
#                 restaurant_attraction_3 = df_a_3.sample(
#                     n=1, weights=df_a_3['weights'])
#             else:
#                 # 如果不符合上述任一條件，就在該區隨機挑選一個景點
#                 filt_a_3 = df_a2['district_num'] == int(selected_district)
#                 df_a_3 = df_a2[filt_a_3]
#                 df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                     lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                 df_a_3['weights'] = df_a_3['rating2'] / \
#                     df_a_3['rating2'].sum()
#                 restaurant_attraction_3 = df_a_3.sample(
#                     n=1, weights=df_a_3['weights'])

# #         filt_a_3 = (df_a2['latitude'] > attraction_2['latitude'].values[0]) & (df_a2['district_num'] == int(selected_district))
# #         df_a_3 = df_a2[filt_a_3]

# #         if df_a_3.shape[0] != 0:
# #             df_a_3['rating2'] = df_a_3['total_rating'].apply(lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
# #             df_a_3['weights'] = df_a_3['rating2'] / df_a_3['rating2'].sum()
# #             attraction_3 = df_a_3.sample(n=1, weights=df_a_3['weights'])
# #         else:
# #             # 如果不符合上述任一條件，就在該區隨機挑選一個景點
# #             filt_a_3 = df_a2['district_num'] == int(selected_district)
# #             df_a_3 = df_a2[filt_a_3]
# #             df_a_3['rating2'] = df_a_3['total_rating'].apply(lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
# #             df_a_3['weights'] = df_a_3['rating2'] / df_a_3['rating2'].sum()
# #             attraction_3 = df_a_3.sample(n=1, weights=df_a_3['weights'])

# else:
#     # 經度差距大於緯度差距，以經度分割
#     if d_longitude > 0:
#         # 如果attraction_1在attraction_2的右邊
#         # 早餐店要篩選longitude > attraction_1的longitude
#         filt_r_1 = (df_r['new_place_category'] == '早午餐') & (
#             df_r['longitude'] > attraction_1['longitude'].values[0]) & (df_r['district_num'] == int(selected_district))
#         df_r_1 = df_r[filt_r_1]
#         if df_r_1.shape[0] != 0:
#             df_r_1['rating2'] = df_r_1['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_1['weights'] = df_r_1['rating2'] / df_r_1['rating2'].sum()
#             restaurant_1 = df_r_1.sample(n=1, weights=df_r_1['weights'])
#         else:
#             filt_r_1 = df_r['district_num'] == int(selected_district)
#             df_r_1 = df_r[filt_r_1]
#             df_r_1['rating2'] = df_r_1['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_1['weights'] = df_r_1['rating2'] / df_r_1['rating2'].sum()
#             restaurant_1 = df_r_1.sample(n=1, weights=df_r_1['weights'])

#         # category_list 接收回傳值
#         category_list = ['中式', '韓式', '台灣小吃/熱炒店', '異國料理',
#                         '港式', '意式', '燒烤店', '南洋', '美式', '火鍋', '素食']
#         if '咖啡甜點' in category_list:
#             category_list_new = category_list.copy()
#             category_list_new.remove('咖啡甜點')
#         else:
#             category_list_new = category_list.copy()
#         category_all = ['中式', '韓式', '台灣小吃/熱炒店', '異國料理',
#                         '港式', '意式', '燒烤店', '南洋', '美式', '火鍋', '素食']

#         # 午餐要選在attraction_1['longitude'] attraction_2['longitude']中間
#         filt_r_2 = df_r[df_r['new_place_category'].isin(category_list_new)]
#         filt_r_2 = filt_r_2[attraction_1['longitude'].values[0]
#                             > filt_r_2['longitude']]
#         filt_r_2 = filt_r_2[attraction_2['longitude'].values[0]
#                             < filt_r_2['longitude']]
#         df_r_2 = filt_r_2[filt_r_2['district_num']
#                             == int(selected_district)]
#         df_r_2.shape[0]

#         if df_r_2.shape[0] != 0:
#             # 如果有在中間
#             df_r_2['rating2'] = df_r_2['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_2['weights'] = df_r_2['rating2'] / df_r_1['rating2'].sum()
#             restaurant_2 = df_r_2.sample(n=1, weights=df_r_2['weights'])
#         else:
#             # 如果不符合上述任一條件，就在該區隨機挑選一間餐廳
#             filt_r_2 = df_r[df_r['new_place_category'].isin(
#                 category_list_new)]
#             df_r_2 = filt_r_2[filt_r_2['district_num']
#                                 == int(selected_district)]
#             df_r_2['rating2'] = df_r_2['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_2['weights'] = df_r_2['rating2'] / df_r_1['rating2'].sum()
#             restaurant_2 = df_r_2.sample(n=1, weights=df_r_2['weights'])

#         # 景點3要篩選longitude < attraction_2的longitude
#         if '咖啡甜點' in category_list:

#             filt_r_3 = (df_r['longitude'] < attraction_2['longitude'].values[0]) & (
#                 df_r['district_num'] == int(selected_district)) & (df_r['new_place_category'] == '咖啡甜點')
#             df_r_3 = df_r[filt_r_3]
#             if df_r_3.shape[0] != 0:
#                 df_r_3['rating2'] = df_r_3['total_rating'].apply(
#                     lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                 df_r_3['weights'] = df_r_3['rating2'] / \
#                     df_r_3['rating2'].sum()
#                 restaurant_attraction_3 = df_r_3.sample(
#                     n=1, weights=df_r_3['weights'])
#             else:
#                 filt_a_3 = (df_a2['latitude'] < attraction_2['latitude'].values[0]) & (
#                     df_a2['district_num'] == int(selected_district))
#                 df_a_3 = df_a2[filt_a_3]
#                 if df_a_3.shape[0] != 0:
#                     df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                         lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                     df_a_3['weights'] = df_a_3['rating2'] / \
#                         df_a_3['rating2'].sum()
#                     restaurant_attraction_3 = df_a_3.sample(
#                         n=1, weights=df_a_3['weights'])
#                 else:
#                     # 如果不符合上述任一條件，就在該區隨機挑選一個景點
#                     filt_a_3 = df_a2['district_num'] == int(
#                         selected_district)
#                     df_a_3 = df_a2[filt_a_3]
#                     df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                         lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                     df_a_3['weights'] = df_a_3['rating2'] / \
#                         df_a_3['rating2'].sum()
#                     restaurant_attraction_3 = df_a_3.sample(
#                         n=1, weights=df_a_3['weights'])

#         else:
#             filt_a_3 = (df_a2['longitude'] < attraction_2['longitude'].values[0]) & (
#                 df_a2['district_num'] == int(selected_district))
#             df_a_3 = df_a2[filt_a_3]

#             if df_a_3.shape[0] != 0:
#                 df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                     lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                 df_a_3['weights'] = df_a_3['rating2'] / \
#                     df_a_3['rating2'].sum()
#                 restaurant_attraction_3 = df_a_3.sample(
#                     n=1, weights=df_a_3['weights'])
#             else:
#                 # 如果不符合上述任一條件，就在該區隨機挑選一個景點
#                 filt_a_3 = df_a2['district_num'] == int(selected_district)
#                 df_a_3 = df_a2[filt_a_3]
#                 df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                     lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                 df_a_3['weights'] = df_a_3['rating2'] / \
#                     df_a_3['rating2'].sum()
#                 restaurant_attraction_3 = df_a_3.sample(
#                     n=1, weights=df_a_3['weights'])

# #         filt_a_3 = (df_a2['longitude'] < attraction_2['longitude'].values[0]) & (df_a2['district_num'] == int(selected_district))
# #         df_a_3 = df_a2[filt_a_3]

# #         if df_a_3.shape[0] != 0:
# #             df_a_3['rating2'] = df_a_3['total_rating'].apply(lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
# #             df_a_3['weights'] = df_a_3['rating2'] / df_a_3['rating2'].sum()
# #             attraction_3 = df_a_3.sample(n=1, weights=df_a_3['weights'])
# #         else:
# #             # 如果不符合上述任一條件，就在該區隨機挑選一個景點
# #             filt_a_3 = df_a2['district_num'] == int(selected_district)
# #             df_a_3 = df_a2[filt_a_3]
# #             df_a_3['rating2'] = df_a_3['total_rating'].apply(lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
# #             df_a_3['weights'] = df_a_3['rating2'] / df_a_3['rating2'].sum()
# #             attraction_3 = df_a_3.sample(n=1, weights=df_a_3['weights'])

#     else:
#         # 如果attraction_1在attraction_2的左邊
#         # 早餐店要篩選longitude < attraction_1的longitude
#         filt_r_1 = (df_r['new_place_category'] == '早午餐') & (
#             df_r['longitude'] < attraction_1['longitude'].values[0]) & (df_r['district_num'] == int(selected_district))
#         df_r_1 = df_r[filt_r_1]
#         if df_r_1.shape[0] != 0:
#             df_r_1['rating2'] = df_r_1['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_1['weights'] = df_r_1['rating2'] / df_r_1['rating2'].sum()
#             restaurant_1 = df_r_1.sample(n=1, weights=df_r_1['weights'])
#         else:
#             filt_r_1 = df_r['district_num'] == int(selected_district)
#             df_r_1 = df_r[filt_r_1]
#             df_r_1['rating2'] = df_r_1['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_1['weights'] = df_r_1['rating2'] / df_r_1['rating2'].sum()
#             restaurant_1 = df_r_1.sample(n=1, weights=df_r_1['weights'])

#         # category_list 接收回傳值
#         category_list = ['中式', '韓式', '台灣小吃/熱炒店', '異國料理',
#                         '港式', '意式', '燒烤店', '南洋', '美式', '火鍋', '素食']
#         if '咖啡甜點' in category_list:
#             category_list_new = category_list.copy()
#             category_list_new.remove('咖啡甜點')
#         else:
#             category_list_new = category_list.copy()
#         category_all = ['中式', '韓式', '台灣小吃/熱炒店', '異國料理',
#                         '港式', '意式', '燒烤店', '南洋', '美式', '火鍋', '素食']

#         # 午餐要選在attraction_1['longitude'] attraction_2['longitude']中間
#         filt_r_2 = df_r[df_r['new_place_category'].isin(category_list_new)]
#         filt_r_2 = filt_r_2[attraction_1['longitude'].values[0]
#                             < filt_r_2['longitude']]
#         filt_r_2 = filt_r_2[attraction_2['longitude'].values[0]
#                             > filt_r_2['longitude']]
#         df_r_2 = filt_r_2[filt_r_2['district_num']
#                             == int(selected_district)]
#         df_r_2.shape[0]

#         if df_r_2.shape[0] != 0:
#             # 如果有在中間
#             df_r_2['rating2'] = df_r_2['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_2['weights'] = df_r_2['rating2'] / df_r_1['rating2'].sum()
#             restaurant_2 = df_r_2.sample(n=1, weights=df_r_2['weights'])
#         else:
#             # 如果不符合上述任一條件，就在該區隨機挑選一間餐廳
#             filt_r_2 = df_r[df_r['new_place_category'].isin(
#                 category_list_new)]
#             df_r_2 = filt_r_2[filt_r_2['district_num']
#                                 == int(selected_district)]
#             df_r_2['rating2'] = df_r_2['total_rating'].apply(
#                 lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#             df_r_2['weights'] = df_r_2['rating2'] / df_r_1['rating2'].sum()
#             restaurant_2 = df_r_2.sample(n=1, weights=df_r_2['weights'])
#         # 景點3要篩選longitude > attraction_2的longitude
#         if '咖啡甜點' in category_list:

#             filt_r_3 = (df_r['longitude'] > attraction_2['longitude'].values[0]) & (
#                 df_r['district_num'] == int(selected_district)) & (df_r['new_place_category'] == '咖啡甜點')
#             df_r_3 = df_r[filt_r_3]
#             if df_r_3.shape[0] != 0:
#                 df_r_3['rating2'] = df_r_3['total_rating'].apply(
#                     lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                 df_r_3['weights'] = df_r_3['rating2'] / \
#                     df_r_3['rating2'].sum()
#                 restaurant_attraction_3 = df_r_3.sample(
#                     n=1, weights=df_r_3['weights'])
#             else:
#                 filt_a_3 = (df_a2['latitude'] < attraction_2['latitude'].values[0]) & (
#                     df_a2['district_num'] == int(selected_district))
#                 df_a_3 = df_a2[filt_a_3]
#                 if df_a_3.shape[0] != 0:
#                     df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                         lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                     df_a_3['weights'] = df_a_3['rating2'] / \
#                         df_a_3['rating2'].sum()
#                     restaurant_attraction_3 = df_a_3.sample(
#                         n=1, weights=df_a_3['weights'])
#                 else:
#                     # 如果不符合上述任一條件，就在該區隨機挑選一個景點
#                     filt_a_3 = df_a2['district_num'] == int(
#                         selected_district)
#                     df_a_3 = df_a2[filt_a_3]
#                     df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                         lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                     df_a_3['weights'] = df_a_3['rating2'] / \
#                         df_a_3['rating2'].sum()
#                     restaurant_attraction_3 = df_a_3.sample(
#                         n=1, weights=df_a_3['weights'])

#         else:
#             filt_a_3 = (df_a2['longitude'] > attraction_2['longitude'].values[0]) & (
#                 df_a2['district_num'] == int(selected_district))
#             df_a_3 = df_a2[filt_a_3]

#             if df_a_3.shape[0] != 0:
#                 df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                     lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                 df_a_3['weights'] = df_a_3['rating2'] / \
#                     df_a_3['rating2'].sum()
#                 restaurant_attraction_3 = df_a_3.sample(
#                     n=1, weights=df_a_3['weights'])
#             else:
#                 # 如果不符合上述任一條件，就在該區隨機挑選一個景點
#                 filt_a_3 = df_a2['district_num'] == int(selected_district)
#                 df_a_3 = df_a2[filt_a_3]
#                 df_a_3['rating2'] = df_a_3['total_rating'].apply(
#                     lambda x: x*2 if x >= 4.3 else (x/2 if x <= 3.7 else x))
#                 df_a_3['weights'] = df_a_3['rating2'] / \
#                     df_a_3['rating2'].sum()
#                 restaurant_attraction_3 = df_a_3.sample(
#                     n=1, weights=df_a_3['weights'])

# df = pd.concat([df, restaurant_1])
# df = pd.concat([df, attraction_1])
# df = pd.concat([df, restaurant_2])
# df = pd.concat([df, attraction_2])
# df = pd.concat([df, restaurant_attraction_3])

# # 最後合併完 reset index
# df = df.reset_index(drop=True)

# # # --------------------------------------------------------------------------------

# print(df[['place_name']])

# url_list = df['place_name'].tolist()

# url=''

# for l in url_list:
#     url += '/' + l

# final_url = 'https://www.google.com.tw/maps/dir' + url 

# print(final_url)