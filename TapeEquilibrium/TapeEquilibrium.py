def solution(A):
    # write your code in Python 3.6
    ans = [] 
    header = 0
    total = sum(A)

    for i in range(len(A)-1):
        header += A[i]
        total -= A[i]
        ans.append(abs(header-total))

    return min(ans)
