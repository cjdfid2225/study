import csv
from cProfile import Profile
from pstats import Stats

# csv파일 불러오기
def open_csv():
    f = open('rowdata.csv','r',encoding='utf-8')
    rdr = csv.reader(f)
    return rdr

# csv파일의 각각의 row를 리스트로 만들기
def make_list(rdr):
    seoul_metro_log = []
    for line in rdr:
        seoul_metro_log.append(line)
    return seoul_metro_log

# 코드 실행

def test():
    ret = open_csv()
    listdata = make_list(ret)
    print(listdata)

profiler = Profile()
profiler.runcall(test)

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats(5)


### csv파일은 여는데 걸린 시간 : 2.3초