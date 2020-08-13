from cProfile import Profile
from pstats import Stats

def my_utility(a,b):
    pass

def first_func():
    for _ in range(1000):
        my_utility(4,5)

def second_func():
    for _ in range(10):
        my_utility(1,3)

def my_program():
    for _ in range(20):
        first_func()
        second_func()

def test(): return my_program()

profiler = Profile()
profiler.runcall(test)  # test()라고 치면 안된다 >> parameter가 있는 함수는 runcall에 쓸 수 없다!
stats = Stats(profiler)
stats.strip_dirs() # dir(파일 경로)을 제거해준다
stats.sort_stats('cumulative')
stats.print_stats(10)
# tottime:총 시간 // percall: 한 번 반복시 걸린 시간 //
# cumtime: 하위 function들까지 고려한 시간 // percall: 하위 function들까지 고려해서 한번 반복시 걸린 시간