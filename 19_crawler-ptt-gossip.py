# .r-ent 貼文總覽, return: list() of post_html
def get_post(html):
    return

# .nrec 推文數量
def get_push(post_html):
    return 

# .author 作者名稱
def get_author(post_html):
    return

# .title 分類 + 文章標題
def get_title(post_html):
    return

# .date 日期
def get_date(post_html):
    return

# 將爬到的標題寫進csv，並print出來
def write_result():
    return

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
    pass

'''
<div class="r-ent">
    <div class="nrec"><span class="hl f2">3</span></div>
    <div class="title">
        <a href="/bbs/Gossiping/M.1579684896.A.B64.html">Re: [問卦] 我大膽預言</a>
    </div>
    <div class="meta">
        <div class="author">CavendishJr</div>
        <div class="article-menu">
            <div class="trigger">&#x22ef;</div>
            <div class="dropdown">
                <div class="item"><a href="/bbs/Gossiping/search?q=thread%3A%5B%E5%95%8F%E5%8D%A6%5D&#43;%E6%88%91%E5%A4%A7%E8%86%BD%E9%A0%90%E8%A8%80">搜尋同標題文章</a></div>
                <div class="item"><a href="/bbs/Gossiping/search?q=author%3ACavendishJr">搜尋看板內 CavendishJr 的文章</a></div>               
            </div>      
        </div>
        <div class="date"> 1/22</div>
        <div class="mark"></div>
    </div>
</div>

<div class="r-ent">
    <div class="nrec"><span class="hl f2">3</span></div>
    <div class="title">
    
        (本文已被刪除) [fatslave]
    
    </div>
    <div class="meta">
        <div class="author">-</div>
        <div class="article-menu"></div>
        <div class="date"> 1/22</div>
        <div class="mark"></div>
    </div>
</div>
'''