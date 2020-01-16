# 讀取檔案
# 一行一行的讀取出來，並計算總合
# r+: Opens a file for reading and writing, placing the pointer at the beginning of the file.
sum = 0
with open("12_file/num.txt", mode="r+") as file:
    for line in file:
        sum += int(line)
print(sum)