#https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling): 
    babbling_lists = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    
    for ii in range(len(babbling)): #babbling의 개수만큼 반복
        for nn in babbling_lists:
            if nn in babbling[ii]: #babbling 인덱싱한게 babbling리스트 안에 해당하는 거면 '!'으로 변경
                babbling[ii] = babbling[ii].replace(nn,'!')
        #제한사항에 babbling들이 최대 한번씩 밖에 못나온다고했으니까 바뀐 '!'로만 리스트가 채워져있으면 구하려고하는 값임
        if babbling[ii] == '!' or babbling[ii] == '!!' or babbling[ii] == '!!!' or  babbling[ii] == '!!!!': 
            answer += 1
    
    return answer


print(solution(['ye','serwr','ayaye','ayayewooma'])) #예시

#49분 6초
