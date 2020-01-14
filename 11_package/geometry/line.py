# 兩點距離
def len(x1, y1, x2, y2):
    return ( (x2-x1)**2 + (y2-y1)**2 )**0.5

# 直線斜率
def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)