import csv

with open('files/ptt-gossiping.csv', newline='', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    for row in rows:
        for col in row:
            print(col, end=' ')