# Point 的實體物件設計: 座標平面上的 x y 點
class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # methods
    def show(self):
        print("X:" + str(self.x) + ", y:" + str(self.y))

    def distance(self, target_x, target_y):
        return ( (self.x - target_x)**2 + (self.y - target_y)**2 )**0.5
    
p = Point(3, 4)
p.show() # method call
dis = p.distance(0, 0) # 計算p座標和原點的距離
print(dis)

# File 的實體物件設計: 包裝檔案讀取的物件
class File:
    # constructor
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None # 初始時沒有開啟的檔案，設 None

    # methods. Only read() need to be call.
    def open(self):
        self.file = open(self.file_name, mode = "r", encoding = "utf-8")
    def close(self):
        self.file.close()
    def read(self):
        self.open()
        content = self.file.read()
        self.file.close()
        return content

# 讀取第一個檔案
f1 = File("files/data.txt")
data = f1.read()
print("\n", data)

# 讀取第二個檔案
f2 = File("files/data2.txt")
data = f2.read()
print("\n", data)