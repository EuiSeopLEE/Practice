#https://school.programmers.co.kr/learn/courses/30/lessons/120875

def solution(dots):
    answer = 0
    
    x_AB = dots[1][0] - dots[0][0]
    x_CD = dots[3][0] - dots[2][0]
    x_AC = dots[2][0] - dots[0][0]
    x_BD = dots[3][0] - dots[1][0]
    x_AD = dots[3][0] - dots[0][0]
    x_BC = dots[2][0] - dots[1][0]
    y_AB = dots[1][1] - dots[0][1]
    y_CD = dots[3][1] - dots[2][1]
    y_AC = dots[2][1] - dots[0][1]
    y_BD = dots[3][1] - dots[1][1]
    y_AD = dots[3][1] - dots[0][1]
    y_BC = dots[2][1] - dots[1][1]
    
    #A,B,C,D가 한 직선상에 있어서 기울기가 일치할 때
    if ((x_AB == x_CD) and (y_AB == y_CD)) and ((x_AC == x_BD) and (y_AC == y_BD)) and ((x_AD == x_BC) and (y_AD == y_BC)): 
        answer += 1
    
    #A,B,C,D가 한 직선상에 있지 않을 때
    elif x_AB == x_CD and y_AB == y_CD:
        answer += 1
    elif x_AC == x_BD and y_AC == y_BD:
        answer += 1
    elif x_AD == x_BC and y_AD == y_BC:
        answer += 1
    else:
        answer = 0
    
    #계산된 answer값들을 제시된 반환값으로 바꿔주기 위한 연산
    if answer > 0:
        answer = 1
    else:
        answer = 0
    
    return answer

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]])) #평행 예시
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]])) #비평행 예시
print(solution([[0, 0], [1, 1], [2, 2], [3, 3]])) #일직선 예시

#22분 32초
