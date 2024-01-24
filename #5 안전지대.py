#https://school.programmers.co.kr/learn/courses/30/lessons/120866

import numpy as np

N = int(input('행렬을 지정해주세요: '))

board = np.random.randint(0, 2, size = (N, N))

def checking_vertex(board): #꼭지점 확인
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0: #(0,0)
                if board[i][j] == 0:
                    pass
                elif board[i][j] == 1:
                    board[i][j] += 2 #self
                    board[i][j+1] += 2 #right
                    board[i+1][j] += 2 #down
                    board[i+1][j+1] += 2 #down right
                else:
                    if board[i][j] % 2 == 0:
                        pass
                    elif board[i][j] % 2 == 1:
                        board[i][j] += 2 #self
                        board[i][j+1] += 2 #right
                        board[i+1][j] += 2 #down
                        board[i+1][j+1] += 2 #down right
                    
            elif i == 0 and j == N-1: #(0,N)
                if board[i][j] == 0:
                    pass
                elif board[i][j] == 1:
                    board[i][j] += 2 #self
                    board[i][j-1] += 2 #left
                    board[i+1][j-1] += 2 #down left
                    board[i+1][j] += 2 #down
                else:
                    if board[i][j] % 2 == 0:
                        pass
                    elif board[i][j] % 2 == 1:
                        board[i][j] += 2 #self
                        board[i][j-1] += 2 #left
                        board[i+1][j-1] += 2 #down left
                        board[i+1][j] += 2 #down
            
            elif i == N-1 and j == 0: #(N,0)
                if board[i][j] == 0:
                    pass
                elif board[i][j] == 1:
                    board[i][j] += 2 #self
                    board[i][j+1] += 2 #right
                    board[i-1][j] += 2 #up
                    board[i-1][j+1] += 2 #up right
                else:
                    if board[i][j] % 2 == 0:
                        pass
                    elif board[i][j] % 2 == 1:
                        board[i][j] += 2 #self
                        board[i][j+1] += 2 #right
                        board[i-1][j] += 2 #up
                        board[i-1][j+1] += 2 #up right
            
            elif i == N-1 and j == N-1: #(N,N)
                if board[i][j] == 0:
                    pass
                elif board[i][j] == 1:
                    board[i][j] = +1 #self
                    board[i][j-1] = +1 #left
                    board[i-1][j] = +1 #up
                    board[i-1][j-1] = +1 #up left
                else:
                    if board[i][j] % 2 == 0:
                        pass
                    elif board[i][j] % 2 == 1:
                        board[i][j] = +1 #self
                        board[i][j-1] = +1 #left
                        board[i-1][j] = +1 #up
                        board[i-1][j-1] = +1 #up left
                
                    

def checking_edge(board): #테두리 확인
    for i in range(N):
        for j in range(N):
            if i == 0 and (1 <= j <= N-2): #top side
                if board[i][j] == 0:
                    pass
                elif board[i][j] == 1:
                    board[i][j] += 2 #self
                    board[i][j-1] = +2 #left
                    board[i][j+1] += 2 #right
                    board[i+1][j-1] += 2 #down left
                    board[i+1][j] += 2 #down
                    board[i+1][j+1] += 2 #down right
                else:
                    if board[i][j] % 2 == 0:
                        pass
                    elif board[i][j] % 2 == 1:
                        board[i][j] += 2 #self
                        board[i][j-1] = +2 #left
                        board[i][j+1] += 2 #right
                        board[i+1][j-1] += 2 #down left
                        board[i+1][j] += 2 #down
                        board[i+1][j+1] += 2 #down right
            
            elif i == N-1 and (1 <= j <= N-2): #bottom side
                if board[i][j] == 0:
                    pass
                elif board[i][j] == 1:
                    board[i][j] += 2 #self
                    board[i][j-1] += 2 #left
                    board[i][j+1] += 2 #right
                    board[i-1][j-1] += 2 #up left
                    board[i-1][j] += 2 #up
                    board[i-1][j+1] += 2 #up right
                else:
                    if board[i][j] % 2 == 0:
                        pass
                    elif board[i][j] % 2 == 1:
                        board[i][j] += 2 #self
                        board[i][j-1] += 2 #left
                        board[i][j+1] += 2 #right
                        board[i-1][j-1] += 2 #up left
                        board[i-1][j] += 2 #up
                        board[i-1][j+1] += 2 #up right
            
            elif (1 <= i <= N-2) and j == 0: #left side
                if board[i][j] == 0:
                    pass
                elif board[i][j] == 1:
                    board[i][j] += 2 #self
                    board[i-1][j] += 2 #up
                    board[i+1][j] += 2 #down
                    board[i-1][j+1] += 2 #up right
                    board[i][j+1] += 2 #right
                    board[i+1][j+1] += 2 #down right
                else:
                    if board[i][j] % 2 == 0:
                        pass
                    elif board[i][j] % 2 == 1:
                        board[i][j] += 2 #self
                        board[i-1][j] += 2 #up
                        board[i+1][j] += 2 #down
                        board[i-1][j+1] += 2 #up right
                        board[i][j+1] += 2 #right
                        board[i+1][j+1] += 2 #down right
            
            elif (1<= i <= N-2) and j == N-1: #right side
                if board[i][j] == 0:
                    pass
                elif board[i][j] == 1:
                    board[i][j] += 2 #self
                    board[i-1][j] += 2 #up
                    board[i+1][j] += 2 #down
                    board[i-1][j-1] += 2 #up left
                    board[i][j-1] += 2 #left
                    board[i+1][j-1] += 2 #down left
                else:
                    if board[i][j] % 2 == 0:
                        pass
                    elif board[i][j] % 2 == 1:
                        board[i][j] += 2 #self
                        board[i-1][j] += 2 #up
                        board[i+1][j] += 2 #down
                        board[i-1][j-1] += 2 #up left
                        board[i][j-1] += 2 #left
                        board[i+1][j-1] += 2 #down left
                    
                    
def checking_normal(board): #꼭지점, 테두리 제외
    for i in range(N):
        for j in range(N):
            if (1 <= i <= N-2) and (1 <= j <= N-2):
                if board[i][j] == 0:
                    pass
                elif board[i][j] == 1:
                    board[i][j] += 2 #self
                    board[i-1][j-1] += 2 #up left
                    board[i-1][j] += 2 #up
                    board[i-1][j+1] += 2 #up right
                    board[i][j-1] += 2 #left
                    board[i][j+1] += 2 #right
                    board[i+1][j-1] += 2 #down left
                    board[i+1][j] += 2 #down
                    board[i+1][j+1] += 2 #down right
                else:
                    if board[i][j] % 2 == 0:
                        pass
                    elif board[i][j] % 2 == 1:
                        board[i][j] += 2 #self
                        board[i-1][j-1] += 2 #up left
                        board[i-1][j] += 2 #up
                        board[i-1][j+1] += 2 #up right
                        board[i][j-1] += 2 #left
                        board[i][j+1] += 2 #right
                        board[i+1][j-1] += 2 #down left
                        board[i+1][j] += 2 #down
                        board[i+1][j+1] += 2 #down right
                    
                             
def solution(board):
    checking_normal(board)
    checking_edge(board)
    checking_vertex(board)
    
    answer = 0
    
    ii = board.tolist()
    
    for nn in range(len(board)):
        zero_count = ii[nn].count(0)
        answer = answer + zero_count
    
    return answer

print(solution(board))

#3시간 34분
