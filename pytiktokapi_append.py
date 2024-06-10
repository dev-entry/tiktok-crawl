from TikTokAPI import TikTokAPI
import json
from pprint import pprint
import time
import csv

cookie = {
    "s_v_web_id": "verify_lx68ref5_cE0ltpd7_ijuS_4TVi_92jI_CGEor2Q1sfEf",
    "ttwid": "1%7CNMqIU7HAs3IT27yC6yW3GhFYPESKsAS-xIBZDijisV8%7C1717865996%7C4f90ecaba504b5a60d76d92e9c200f7928fe029ca3f086e7cf36a54f7ba7376b",
}

api = TikTokAPI(cookie=cookie)

# example data
# {
#         "avatarLarger": "https://p16-sign-sg.tiktokcdn.com/aweme/1080x1080/tos-alisg-avt-0068/a445d7462de08db5adc8138db21afab7.jpeg?lk3s=a5d48078&nonce=27800&refresh_token=44b2a619d44d266140e36d044fcaeae9&x-expires=1718132400&x-signature=9LVzTGwOk6k4xxlnylnWKmQBYV0%3D&shp=a5d48078&shcp=b59d6b55",
#         "avatarMedium": "https://p16-sign-sg.tiktokcdn.com/aweme/720x720/tos-alisg-avt-0068/a445d7462de08db5adc8138db21afab7.jpeg?lk3s=a5d48078&nonce=68031&refresh_token=c974782a50de7b1d69ccded882a0501c&x-expires=1718132400&x-signature=Mk0FO7J25tHPVJr2INMWPsYfE2g%3D&shp=a5d48078&shcp=b59d6b55",
#         "avatarThumb": "https://p16-sign-sg.tiktokcdn.com/aweme/100x100/tos-alisg-avt-0068/a445d7462de08db5adc8138db21afab7.jpeg?lk3s=a5d48078&nonce=87046&refresh_token=5c80e943fa0dde360b809af2bb778b6a&x-expires=1718132400&x-signature=Xf1tCo6m3cJ%2BlCiCFRx1OXziPBc%3D&shp=a5d48078&shcp=b59d6b55",
#         "commentSetting": 0,
#         "downloadSetting": 0,
#         "duetSetting": 0,
#         "ftc": false,
#         "id": "7108406776059905030",
#         "isADVirtual": false,
#         "isEmbedBanned": false,
#         "nickname": "Garima Ramjali \u271d\ufe0f",
#         "openFavorite": false,
#         "privateAccount": false,
#         "relation": 0,
#         "secUid": "MS4wLjABAAAAQeDYdd_2cMJ0WGVn76ByUKvhjM8PeeNUZakl1npCTzugvdJHWbWveNPSjXIfeJcv",
#         "secret": false,
#         "signature": "\u0928\u092f\u093e \u0917\u093f\u0924 : \u0939\u0941\u0928\u094d\u0928 \u0905\u092c \u0924 \ud83c\udfb6\nFecebook : Garima Ramjali\nYouTube: Garima Ramjali \ud83d\ude4f\u2764\ufe0f\ud83e\udec2",
#         "stitchSetting": 0,
#         "ttSeller": false,
#         "uniqueId": "garimaramjali8",
#         "verified": false,
#         "diggCount": 2499,
#         "followerCount": 92600,
#         "followingCount": 53,
#         "friendCount": 0,
#         "heart": 3000000,
#         "heartCount": 3000000,
#         "videoCount": 2098
#     },

titoker_ids = []

with open("tiktokers_appending.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == "avatarLarger":
            continue
        titoker_ids.append(row[19])


for _ in range(10000):
    retval = api.getTrending(count=100)
    if not retval:
        break
    items = retval.get("items", [])
    for item in items:
        author = item.get("author", {})
        author_stats = item.get("authorStats", {})
        author.update(author_stats)
        if author["uniqueId"] not in titoker_ids:
            titoker_ids.append(author["uniqueId"])

            with open("tiktokers_appending.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(
                    [
                        author.get("avatarLarger", ""),
                        author.get("avatarMedium", ""),
                        author.get("avatarThumb", ""),
                        author.get("commentSetting", ""),
                        author.get("downloadSetting", ""),
                        author.get("duetSetting", ""),
                        author.get("ftc", ""),
                        author.get("id", ""),
                        author.get("isADVirtual", ""),
                        author.get("isEmbedBanned", ""),
                        author.get("nickname", "").replace("\n", " "),
                        author.get("openFavorite", ""),
                        author.get("privateAccount", ""),
                        author.get("relation", ""),
                        author.get("secUid", ""),
                        author.get("secret", ""),
                        author.get("signature", "").replace("\n", " "),
                        author.get("stitchSetting", ""),
                        author.get("ttSeller", ""),
                        author.get("uniqueId", ""),
                        author.get("verified", ""),
                        author.get("diggCount", ""),
                        author.get("followerCount", ""),
                        author.get("followingCount", ""),
                        author.get("friendCount", ""),
                        author.get("heart", ""),
                        author.get("heartCount", ""),
                        author.get("videoCount", ""),
                    ]
                )

    time.sleep(2)
