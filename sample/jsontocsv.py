import csv
import json

input_file_name = "sample/PBDS.csv"
output_file_name = "sample/json.txt"
#with open(input_file_name, "r", encoding="utf-8", newline="") as input_file, \
#        open(output_file_name, "w", encoding="utf-8", newline="") as output_file:
#                           !!! w라는 옵션은 파일이 없으면 파일을 생성한다!!!

input_file = open(input_file_name, "r", encoding="utf-8", newline="")
output_file = open(output_file_name, "w", encoding="utf=-8", newline="")
#위처럼 써도 똑같은 의미.

reader = csv.reader(input_file)
#첫 줄은 col_names 리스트로 읽어놓고
col_names = next(reader)
#그 다음 줄부터 zip으로 묶어서 json으로 dumps 

for cols in reader:
    #doc = dict(zip(col_names,cols))
    doc = {
           col_name: col for col_name, col in zip(col_names,cols)}
    print(json.dumps(doc, ensure_ascii = False),file=output_file)
            #json파일로 변경시 dumps함수를 쓴다.
