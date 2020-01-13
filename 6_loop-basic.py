# while基本句型
while False:
    pass

# for基本句型
for i in [1,4,2,3]: # traverse in list
    pass
for c in 'Hello': # 逐一取得字元
    pass 
for x in range(3): # 相當於 in [0,1,2] 但python3的range()和2代差很多，要轉成list才能直接使用。如list(range(0, 30, 5))
    pass

# while 教學

# 1) 無窮迴圈
# n = 1
# while True:
#     print(n)
#     n += 1

# 2) 等差級數加總
n = 1
sum = 0
while n <= 10:
    sum += n
    n += 1
print(sum)

# for 教學
n = 1
sum = 0
for i in range(1, 11):
    sum += i
print(sum)