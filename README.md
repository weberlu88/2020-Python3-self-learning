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

**13. Random statistics**
* Random
  * `random.random()`
  * `random.uniform(0.0, 1.0)`
  * `random.normalvariate(100, 10)`
* Statistics
  * `statistics.mean(list)`
  * `statistics.median(list)`
  * `statistics.stdev(list)`
