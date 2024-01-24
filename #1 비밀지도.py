#2018 카카오 코딩 블라인드테스트 1번
#https://school.programmers.co.kr/learn/courses/30/lessons/17681

import random #난수를 위한 랜덤모듈

n = int(input('정사각형 한변의 크기를 지정해주세요: ')) #정사각형의 크기 지정

arr1 = []
arr2 = []
for ii in range(0, n) : 
    var1 = random.randint(0, 2**n - 1) #정사각형 배열1에 들어갈 숫자 임의 지정
    arr1.append(var1)


for ss in range(0, n) : 
    var2 = random.randint(0, 2**n - 1) #정사각형 배열2에 들어갈 숫자 임의 지정
    arr2.append(var2)


lists1 = []
lists2 = []


# 자리수를 고려하여 10진수 arr -> 2진수 arr로 변환하는 함수
def converted_2(arr, lists) :
    for m in arr : 
        add_lists1 = [] #리스트 초기화
        for kk in range((n-1), -1, -1) :
            a = 2 ** kk
            if m - a < 0  : 
                add_lists1.append(False)
            else:
                add_lists1.append(True)
                m -= a 
        lists.append(add_lists1)
    return lists


arr1 = converted_2(arr1, lists1) #2진수로 변환된 리스트1
arr2 = converted_2(arr2, lists2) #2진수로 변환된 리스트2




def solution_func(arr1, arr2) : #풀이 함수
    answer_lists = [] #최종 지도값이 나올 리스트
    for pp in range(0, n) : #2진수로 변환된 arr1 과 arr2 리스트의 첫 인덱스끼리 비교하는 반복문
        add_lists2 = '' #초기화
        x = arr1[pp]
        y = arr2[pp]
        for nn in range(0, n) : #뽑은 첫 인덱스 리스트 안의 요소끼리 비교하는 반복문
            w = x[nn]
            z = y[nn]
            if (w == False) and (z == False) : #둘 다 False일 때만 공백이고 나머지는 전부 #벽처리
                add_lists2 += " "
            else: 
                add_lists2 += "#"
        answer_lists.append(add_lists2) #최종 리스트에 '#'과 ' '으로 출력된 리스트 추가
    return print(answer_lists)

solution_func(arr1, arr2)
