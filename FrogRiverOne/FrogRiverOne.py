def solution(X, A):
    # write your code in Python 3.6
    set_A = list(set(A))

    if len(set_A) != X:
        return -1
    
    cnt = 0
    dic = {}
    for i in range(len(A)):
        if dic.get(A[i]) == None:
            dic[A[i]] = 1
            cnt += 1
        else:
            pass
        
        if cnt == X:
            return i
