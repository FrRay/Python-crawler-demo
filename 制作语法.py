import requests
import re

# 原神二创图片排行榜
url = "https://bbs-api.mihoyo.com/post/wapi/forum/rank/post/list"

# 排行榜月份，默认2022年2月，可以改成202201
monthDate = 202202

param = {
    "forum_id": '29',
    'gids': '2',
    'rank_date': monthDate,
    'size': '40',
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
}

# 得到响应体
resp = requests.get(url=url, headers=headers, params=param)

# 响应体转成字符串
page_content = resp.text

# 解析数据(正则表达式)
obj = re.compile(
    r'subject":"(?P<title>.*?)","content.*?cover":"(?P<picurl>.*?)","view_type', re.S)

# 开始匹配
result = obj.finditer(page_content)
f = open("_MHYdata.txt", mode="w", encoding="utf-8")

# 写出匹配结果(标题+url)
for it in result:
    f.write(it.group("title"))
    f.write("\t\t:\t")
    f.write(it.group("picurl"))
    f.write("\n")
    # 也可以保存全部图片(标题+图片)
    resp1 = requests.get(it.group("picurl"))
    with open(it.group("title")+'.jpg', 'wb') as p:
        p.write(resp1.content)
        resp1.close()

f.close()
resp.close()
