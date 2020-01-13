# Section1.數字運算
x = 2*3
y = 2**3 # power
z = 2**0.5 # Square root
u = 5%1

x = x + 1
x += 1
# x++ # Noooo!

# Section2.字串運算
str1 = "Hell\"o "
str2 = "Hell\"o " + 'world'
str2 = "Hell\"o " 'world' # 空白等於串接
str3 = """Hello


World""" # 3個引號內任意換行
str4 = 'Hello'*3 +'World'
print(str4)

# 字串會對內部的字元編號(index索引)，從0開始算起
string1 = 'MISbetterthanCS'
print( string1[1] ) #[0] > M, [1] > I...
print( string1[3:] ) #從index=3到結尾的字串 > betterthanCS
print( string1[:3] ) #從開頭到index=3的字串 > MIS