import json
import csv

input_file_name = "sample/json.txt"
output_file_name = "sample/test.csv"
with open(input_file_name, "r", encoding="utf-8", newline="") as input_file, \
        open(output_file_name, "w", encoding="utf-8", newline="") as output_file:
#w라는 옵션은 파일이 없으면 파일을 생성한다!!!

    data = []
    for line in input_file:
        datum = json.loads(line)
        data.append(datum)

    csvwriter = csv.writer(output_file)
    csvwriter.writerow(data[0].keys()) #writerow: csv로 만들건데 한줄한줄 써넣을거라는 의미의 함수
    for line in data:
        csvwriter.writerow(line.values())