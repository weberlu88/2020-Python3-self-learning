# 參數的預設資料
def power(base, exp = 0):
    res = base**exp
    print(res)
    return res

power(3, 2)

# 使用參數名稱對應
def divide(n1, n2):
    res = n1/n2
    print(res)
    return res

divide(2, 4)
divide(n2=2, n1=4)

# 無限(不定)參數資料(tuple)
def avg(*ns):
    print(ns)
    sum = 0
    for i in ns:
        sum += i
    else:
        res = sum/len(ns)
        print(res)
    return res

avg(3, 4)
avg(3, 5, 10)
avg(10, -1, 5, -6)