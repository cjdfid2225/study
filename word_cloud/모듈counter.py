from collections import Counter

lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
# print(Counter(lst))


dic = {'가':3, '나':2, '다':4}
# print(Counter(dic))
# 딕셔너리여도 정렬된다

# dic.get('key값',0) : value값 호출 == dic['key값']
# cf) 존재하지 않는 key를 호출시
# dic['라'] -> 에러                  /////                    dic.get('라',0) -> 0 물론 dic은 변함x
# 즉, dic.get('key값',0) : 해당 key값이 존재하면 그걸 호출해주고, 없으면 0을 호출



counter = Counter()
counter.update("aabbccddeeff") 
# update : 객체에 들어가 있는 값 자체를 변경해주는 함수 >> cc = counter.update("aabbccddeeff")라고 하면 print(cc)=None
# print(counter)
# 분절시킨 후에 숫자 세준다

counter = Counter("aabbccddeeff")
cc = counter.elements()
print(counter)
print(list(cc))

# counter.most_common(): 빈도 수 높은 단어들 호출하는 함수