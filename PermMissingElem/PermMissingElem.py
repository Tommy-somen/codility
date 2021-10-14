def solution(A):
    # write your code in Python 3.6
    len_A = len(A)

    if len_A == 0:
        return 1
    else:

        A.sort()

        for i in range(len_A-1):
            if A[i]+1 != A[i+1]:
                return A[i]+1
        
        if min(A) != 1:
            return 1
        else:
            return max(A)+1
