import urllib.request as req
import bs4 

# This function get all titles in a signle page.
# @retrun next_link: "/bbs/Gossiping/index39154.html"
def getData(url):

    # Step.1 抓取 PTT 八卦版的網頁原始碼 (HTML file)
    # Create a Request object. Need over18's cookie to access Gossoping BBS.
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    })
    with req.urlopen(request) as response:
        html = response.read().decode("utf-8")
    # print(html)

    # Step.2 透過 bs4 解析網頁原始碼，取得每篇文章的標題
    soup = bs4.BeautifulSoup(html, "html.parser")
    # print(soup.title.string)

    # select all class = "title" 的 div 標籤
    title_list = soup.find_all("div", class_ = "title")
    for title in title_list:
        if title.a != None: # includes <a> means post exists
            print(title.a.string)

    # Step.3 抓取上一頁的連結並 return
    next_link = soup.find("a", string = "‹ 上頁") # 搜尋內文是"‹ 上頁"的<a>
    return next_link["href"]

# main codes
def main():
    pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
    
    count = 0
    while count < 3:
        # getData() : /bbs/Gossiping/index39154.html
        pageURL = "https://www.ptt.cc" + getData(pageURL)
        print(pageURL)
        count += 1
    return

if __name__ == "__main__":
    main()
    pass
