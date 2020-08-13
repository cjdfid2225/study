from openpyxl import load_workbook
from cProfile import Profile
from pstats import Stats

# 엑셀 파일 불러오기
def open_xlsx(file):
    load_file = load_workbook(file,data_only=True)
    return load_file

# 엑셀 파일의 시트를 리스트로 만들기
def make_list(file):
    get_rows = file.worksheets[0]
    file_log = []
    for row in get_rows:
        file_log.append(row)
    return file_log

# 코드실행

def runcode():
    filename = "rowdata_sample.xlsx"
    book = open_xlsx(filename)
    data = make_list(book)
    print(data)

profiler = Profile()
profiler.runcall(runcode)

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats(5)


### 엑셀파일은 여는데 걸린 시간: 8분