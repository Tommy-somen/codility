def solution(A):
    # write your code in Python 3.6

    pairs_dic = {}

    for i in range(len(A)):
        if pairs_dic.get(A[i]) == None:
            pairs_dic[A[i]] = 1
        else:
            pairs_dic[A[i]] += 1

    set_A = list(set(A))

    for num in set_A:
        if pairs_dic[num]%2 != 0:
            return num
  
  ################################
  #上記の解法を行った後、もっと短く書けるかと思い、count(A)%2 != 0の方法ですると、
  #計算量最悪(O(n**2))により、余裕でTLEです。
  
