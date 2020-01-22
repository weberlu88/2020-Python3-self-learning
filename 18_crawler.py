'''Step.1 抓取 PTT 電影版的網頁原始碼 (HTML file)'''
# 抓取 PTT 電影版的網頁原始碼 (HTML file)
import urllib.request as req

# Create a Request object, 附加 Request Headers 的資訊, act as browser.
# if 直接用 url 連線 >> HTTP Error 403: Forbidden
url = "https://www.ptt.cc/bbs/movie/index.html" 
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
})

# urlopen() with request object, not url
with req.urlopen(request) as response:
    html = response.read().decode("utf-8")

# print the HTML source code
# print(html)

'''Step.2 透過 bs4 解析網頁原始碼，取得每篇文章的標題'''
# bs4 docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import bs4 

soup = bs4.BeautifulSoup(html, "html.parser")
print(soup.title.string)

# select all class = "title" 的 div 標籤
title_list = soup.find_all("div", class_ = "title")
for title in title_list:
    if title.a != None: # includes <a> means post exists
        print(title.a.string)

# 標題的 div 長這樣：div > a > string
# 被刪除的長這樣：div > string
# <div class="title">
# 	<a href="/bbs/movie/M.1579650163.A.BDA.html">[討論] 誠實預告:小丑2019</a>
# </div>
# <div class="title">
# 	(本文已被刪除) [Lian68]
# </div>