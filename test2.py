import pprint
import json

urlList = ["https://www.google.com.tw/maps/place/%E8%95%83%E8%8C%84%E5%A6%B9%E5%B0%8F%E5%90%83%E5%BA%97/data=!4m7!3m6!1s0x3442a949b3b63957:0x7b22d945beadce01!8m2!3d25.0713438!4d121.5158121!16s%2Fg%2F1td2dls1!19sChIJVzm2s0mpQjQRAc6tvkXZIns?authuser=0&hl=zh-TW&rclk=1", "https://www.google.com.tw/maps/place/%E5%A4%A7%E9%BE%8D%E5%BB%A3%E6%9D%B1%E7%B2%A5/data=!4m7!3m6!1s0x3442a960f1a68bf5:0xbff068f555ca3bfe!8m2!3d25.0667749!4d121.5158718!16s%2Fg%2F11p_1pnfxc!19sChIJ9Yum8WCpQjQR_jvKVfVo8L8?authuser=0&hl=zh-TW&rclk=1", "https://www.google.com.tw/maps/place/Q+Burger+%E5%A4%A7%E5%90%8C%E5%A4%A7%E9%BE%8D%E5%BA%97/data=!4m7!3m6!1s0x3442a91be64e4aed:0xdd7b73af08567716!8m2!3d25.0677692!4d121.5158121!16s%2Fg%2F11k5n4w9gw!19sChIJ7UpO5hupQjQRFndWCK9ze90?authuser=0&hl=zh-TW&rclk=1", "https://www.google.com.tw/maps/place/%E8%80%81%E5%9C%B0%E6%96%B9%E7%89%9B%E8%82%89%E9%BA%B5%E9%A3%9F%E9%A4%A8/data=!4m7!3m6!1s0x3442a9464e6f02cd:0x79f08aa8dae79fd7!8m2!3d25.0673476!4d121.5173978!16s%2Fg%2F1tyks1s4!19sChIJzQJvTkapQjQR15_n2qiK8Hk?authuser=0&hl=zh-TW&rclk=1", "https://www.google.com.tw/maps/place/%E2%80%A2%E5%A3%B9%E6%9F%92%E9%A3%9F%E5%A0%82%E2%80%A2/data=!4m7!3m6!1s0x3442a9b2d94f03c7:0xd5f4285c70a63d22!8m2!3d25.0653876!4d121.5159267!16s%2Fg%2F11q8tjwtqf!19sChIJxwNP2bKpQjQRIj2mcFwo9NU?authuser=0&hl=zh-TW&rclk=1", "https://www.google.com.tw/maps/place/%E8%95%83%E8%8C%84%E5%A6%B9%E5%B0%8F%E5%90%83%E5%BA%97/data=!4m7!3m6!1s0x3442a949b3b63957:0x7b22d945beadce01!8m2!3d25.0713438!4d121.5158121!16s%2Fg%2F1td2dls1!19sChIJVzm2s0mpQjQRAc6tvkXZIns?authuser=0&hl=zh-TW&rclk=1"]  

print(len(set(urlList)))

allurlList = []

allurlList.append({
    "herf": list(set(urlList))
})

pprint.pprint(allurlList)

# with open(f'allurlList.json', 'w', encoding='utf-8') as file:
#             (json.dump(allurlList, file, ensure_ascii=False, indent=4))