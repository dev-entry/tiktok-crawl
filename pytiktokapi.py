from TikTokAPI import TikTokAPI
import json
from pprint import pprint
import time

cookie = {
    "s_v_web_id": "verify_lx68ref5_cE0ltpd7_ijuS_4TVi_92jI_CGEor2Q1sfEf",
    "ttwid": "1%7CNMqIU7HAs3IT27yC6yW3GhFYPESKsAS-xIBZDijisV8%7C1717865996%7C4f90ecaba504b5a60d76d92e9c200f7928fe029ca3f086e7cf36a54f7ba7376b",
}

api = TikTokAPI(cookie=cookie)


titokers = []
titoker_ids = []

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
            titokers.append(author)
            titoker_ids.append(author["uniqueId"])

    time.sleep(2)


with open("tiktokers.json", "w") as f:
    f.write(json.dumps(titokers, indent=4))
