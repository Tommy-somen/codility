from collections import deque

def solution(A, K):
    # write your code in Python 3.6

    if len(A) == 0:
        return []
    else:
        deque_A = deque(A)

    for i in range(K):
        tmp = deque_A.pop()
        deque_A.appendleft(tmp)
        
    return list(deque_A)
