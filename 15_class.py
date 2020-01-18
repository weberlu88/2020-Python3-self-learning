# 定義類別，和類別中的屬性 (attribute包括variable和method)
# 定義類別IO 有一個變數和一個方法
class IO:
    supportedSrc = ["console", "file"]

    def read(src):
        if src not in IO.supportedSrc:
            print("io not support")
        else:
            print("read from", src)

# 使用類別 >> 單純call class裡的變數和方法而已
print(IO.supportedSrc)
IO.read("file")
IO.read("internet")

# warning
# i = IO()
# i.read("file") # 可以new 但是read()沒有加self參數會無法呼叫