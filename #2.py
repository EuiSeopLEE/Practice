#2018 카카오 블라인드 코딩테스트 2번문제

def solution_func(dartResult) : 
    dict1 = {'S' : 1 , 'D' : 2, 'T' : 3} #조건사용(문자에 따른 값을 가지기 때문에 딕셔너리 썼음)

    num = ''
    
    lists = []
    
    for ii in dartResult : #입력값 반복문
        if ii.isdigit() : #입력한 문자열이 숫자인지 아닌지 구분
            num = num + ii
        elif ii in dict1 : 
            if ii == 'S' :
                lists.append(int(num) ** 1)
            if ii == 'D' : 
                lists.append(int(num) ** 2)
            if ii == 'T' : 
                lists.append(int(num) ** 3)
            num = '' #초기화
        elif ii == '*' : #'*'이 나올 경우
            lists[-1] = lists[-1] * 2
            if len(lists) >= 2 : #추가했던 리스트 값 중에 두번째가 존재할 경우
                lists[-2] = lists[-2] * 2
        elif ii == '#' : #'#'이 나올 경우
            lists[-1] = lists[-1] * -1
    return sum(lists)

print(solution_func('10S*10S#10S*')) #예시
