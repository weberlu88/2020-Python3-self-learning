# instance = object
# Point 的實體物件設計: 座標平面上的 x y 點
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Create an object
p1 = Point(0, 0)
print(p1.x, p1.y)

# Create another object
p2 = Point(3, 4)
print(p2.x, p2.y)

# FullName object 的設計
class FullName:
    def __init__(self, first, last):
        self.first = first
        self.last = last

# Create a neme object
n1 = FullName("C.W", "Peng")
print(n1.first, n1.last)