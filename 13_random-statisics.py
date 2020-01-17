# 隨機模組
import random

# 隨機選取list
mylist = [1, 5, 6, 10, 20]
data = random.choice(mylist) # return one item
print("choice():", data)

data = random.sample(mylist, 3) # return a list with 3 random elements
print("sample():", data)

data = [1, 5, 8, 10]
random.shuffle(data) # shuffle input list, no returns
print("shuffle():", data)

# 取得亂數
data = random.random() # return random num 0 ~ 1
print("random():", data)

data = random.uniform(0.0, 1.0) # return random num 0 ~ 1 (均勻分布)
print("uniform(0.0, 1.0):", data)

data = random.uniform(60, 100) # return random num 60 ~ 100
print("uniform(60, 100):", data)

# 取得常態分配的亂數 
# 平均數 u = 100, 標準差 sigma = 10, 66.5% 的機率落於 90~110 之間
data = random.normalvariate(100, 10) 
print("normalvarirate(100, 10):", data)
print("------------")

# 統機模組
import statistics as stat

data = stat.mean([1,2,3,4,5,8,100]) # 平均數
print("mean():", data)

data = stat.median([1,2,3,4,5,8,100]) # 中位數
print("median():", data)

data = stat.stdev([1,2,3,4,5,8,100]) # 標準差
print("stdev():", data)