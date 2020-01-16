# 儲存檔案 mode = "w"
file = open('12_file/data.txt', mode='w', encoding='utf-8')
file.write('Hello world \nSecond line \n中文測試') # 要寫入中文日文德文韓文等，需要 utf-8 編碼
file.close()

# 讀取檔案 mode = "r"
file = open('12_file/data.txt', mode='r', encoding='utf-8') # default 是 read only 不寫 mode 也可以
data = file.read()
print(data)
file.close()

# 上述2者都有 with open as 方法，建議使用務實方法

# 使用 json 格式讀取、覆寫檔案
import json
with open('12_file/config.json', mode='r') as file: 
    data = json.load(file) 

print("json content: ", data) # load() return 一個字典
print("name:", data['name'])
print("version:", data['version'])
    
data['version'] = "1.3.7" # 編輯變數 data 中的 value pair

# 覆寫 json 的所有資料回檔案中
with open('12_file/config.json', mode='w') as file: 
    json.dump(data, file)