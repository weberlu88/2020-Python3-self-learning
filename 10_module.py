# 載入內建的 sys 模組並取得資訊
import sys

print(sys.platform)
print(sys.maxsize)
print(sys.path)
print("--------------")

# 自己建立 10_geometry 模組，載入使用
# import geometry as geo # geo為模組的別名
# res = geo.distance(1,1,5,5)
# print(res)
# res = geo.slope(1,2,5,6)
# print(res)

# 調整搜尋模組的路徑
sys.path.append("modules") # 新增模組路徑
print(sys.path) # 印出模組的搜尋路徑
print("--------------")

import geometry as geo # geo為模組的別名
res = geo.distance(1,1,5,5)
print(res)
res = geo.slope(1,2,5,6)
print(res)