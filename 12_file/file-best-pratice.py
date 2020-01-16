# 最佳實務 - with open
with open('12_file/data.txt', mode='w', encoding='utf-8') as file:
    file.write('Hello world \nSecond line \n中文測試 & 最佳實務法')
