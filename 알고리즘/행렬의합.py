<문제>
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
ex1)
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
return = [[4,6],[7,9]]
ex2)
arr1 = [[1],[2]]
arr2 = [[3],[4]]
return = [[4],[6]]



<답>
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        practice = []
        for j in range(len(arr1[i])):
            practice.append(arr1[i][j]+arr2[i][j])
        answer.append(practice)
    return answer