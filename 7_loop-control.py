# while-else 區塊
n = 1
while n <= 10:
    n += 1
else:
    print('迴圈結束前，必會執行此區塊')

# break的簡易範例 > break不會執行else區塊
n = 0
while n < 5:
    if n == 3:
        break
    print(n) #印出迴圈中的n
    n+=1
print("最後的n: ",n) # 印出迴圈結束的 n

# continue 的簡易範例
n = 0
for x in [0,1,2,3]:
    if x % 2 == 0: # x是偶數 > 忽略下方程式
        continue
    print(x)
    n += 1
print("最後的n: ",n)

# for-else 的簡易範例
sum = 0
for x in range(1,11):
    sum += x
else:
    print(sum) # 印出1+2+3+4+5+6......10的結果

#綜合範例: 找出整數平方根
#輸入9,得到3
#輸入11,得到[沒有]整數的平方根
n=int(input("輸入一個數字"))
for x in range(n+1):
    if x**2 == n:
        print(n,"的整數平方根是",x)
        break #break強制結束迴圈時候,不會執行else區塊
else:
    print(n,"沒有整數平方根")