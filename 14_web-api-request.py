# What are the differences between the urllib, urllib2, urllib3 and requests module?
# https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-urllib3-and-requests-modul?fbclid=IwAR0tv3zR2Dx3VzP2VUyWqpfyEKVNgra_VATpJb8OLBJ0TTXPjP5uMyJvYe0

# 網路連線
import urllib.request as request
import json

src = "https://www.ntu.edu.tw/"
with request.urlopen(src) as response:
    data = response.read().decode("utf-8") # 取得台大網站的首頁原始碼。需要decode()轉編碼
# print(data)

# 以get方法取得公開資料 (只透過url)
src = "http://data.taipei/" # 台北市政府公開資料
src = "https://jsonplaceholder.typicode.com/posts" # test api
with request.urlopen(src) as response:
    plist = json.load(response) # 處理json格式，轉為dict物件
# print(data)

# 取出post的title和id
# for post in plist:
#     post_id = post["id"]
#     title = post["title"]
#     print()

# 將post標題寫入檔案
with open("files/post_list.txt", mode = "w") as file:
    for post in plist:
        file.write(post["title"]+"\n")