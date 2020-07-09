import csv
f = open('2020년 06월  교통카드 통계자료.csv')
data = csv.reader(f)

rate = 0
mx_row = []
rate_dict = {}

for row in data:
    if data.line_num == 1:
        continue
    for i in range(4, 8):
        row[i] = row[i].replace(",", "")
        row[i] = int(row[i])
    if row[6] != 0:
        rate = row[4]/row[6]
        rate_dict[row[3]]=rate

rate_list = sorted(rate_dict, key=lambda k : rate_dict[k], reverse=True)
print(rate_list[0:3])