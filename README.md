# 2020-Python3-self-learning

The youtube channel I follow:  
> Python 入門教學課程  
> https://www.youtube.com/playlist?list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&amp;fbclid=IwAR1cfyv1iN6JaAVKfZUc4Qk4fmVJFjz-sPmsfkJNJOvTLQ6CH9Hz4idY6sk

---

## Topics
  1. Datatype
  2. Number string
  3. List tuple
  4. Set dictionary
  5. Condition
  6. Loop basic
  7. Loop control
  8. Functon basic
  9. FunCtion args
  10. Module
  11. Package
  12. File
  13. Random statistics

---

## Details

**4. Set-dictionary**
* set1 & set2 means 聯集
* set1 | set2 means 交集
* set1 - set2 means 差擊
* set1 ^ set2 means 反交集
* `var in set` `var not in set` will return `True` `False`
* 從列表的資料中產生字典`dic={x:x*2 for x in [3,4,5]}` 

**5. Condition**
* 單一判斷：if ...
* 雙向判斷：if ... else
* 多條件判斷：if ... elif ... else ...

**6. Loop basic**
* for loop
* while loop

**7. Loop control**
* break continue else
* else區塊像是try-catch的finally區塊，迴圈結束前，必會執行else區塊
* 但break之後不會執行else區塊

**9. Funtion args**
* 預設參數值
* 使用參數名稱對應
* 無限(不定)參數資料(tuple)

**10. Module**

**12. File**
* 讀寫檔案的3步流程：開檔 > 讀/寫 > 關檔。如果不關閉檔案會占用使用狀態，因為每個檔案一次只能一個被thread(?)讀取
* 讀取檔案的方式：
  * 文字格式：一行一行讀 `object = file.read()` `for line in object: ...`
  * json格式：一次讀取全部 `data = json.load(fileObject)`
  * csv格式：一次讀取全部
  * open modes：https://stackabuse.com/file-handling-in-python/
* 寫入檔案的方式：
  * 文字格式：一次覆寫全部 `fileObject = file.write(String)`
  * json格式：一次覆寫全部 `json.dump(data, fileObject)`
  * csv格式：一次覆寫全部
* 關閉檔案：`fileObject.close()`
* 最佳實務方法：`with open(path, mode=) as fileObject:`
  * 會自動且安全的關閉檔案
  * 類似try-catch在try中的連線方法

**13. Random-statistics**
* Random 模組
  * 隨機選取：choice()、sample()
  * 隨機調換順序：shuffle()
  * 取得隨機亂數：random()、uniform()
  * 取得常態分配亂數：normalvariate()
  
* Statistics 模組
  * 計算平均數：mean()
  * 計算中位數：median()
  * 計算標準差：stdev()

**14. API request**
* https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-urllib3-and-requests-modul?fbclid=IwAR0tv3zR2Dx3VzP2VUyWqpfyEKVNgra_VATpJb8OLBJ0TTXPjP5uMyJvYe0
* urllib.request module document: https://docs.python.org/3/library/urllib.request.html
* requests module document:https://requests.readthedocs.io/en/master/
* 網路連線程式，以 HTTP 通訊協定為例
  * 使用 urllib.request 模組
  * 使用 urlopen(網址) 連線網址
  * 使用 read() 讀取資料
  * 使用 decode("utf-8")  處理中文資料
  * 使用 json 模組，解讀 json 資料格式

* 公開資料串接
  * 使用台北市政府公開資料 (http://data.taipei/)
  * 搜尋並取得資料的串接網址 (API)
  * 測試串接網址，觀察資料格式
  * 撰寫程式，自動連線並且擷取想要的資料

* 儲存資料到檔案中
  * 使用寫入模式開啟檔案
  * 使用 utf-8 編碼處理中文資料

**15. Class**
* 使用 class 建立類別
* 建立類別的屬性 ( 封裝在類別中的變數或函式 )
* 使用類別的基本語法：類別名稱.屬性名稱 > 直接 call class 的屬性