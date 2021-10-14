def solution(n):
    # write your code in Python 3.6

    bin_n = bin(n)
    seq_bin_n = list(str(bin_n))

    ans = [0]
    one_count = 0
    zero_count = 0

    for i in range(len(seq_bin_n)):
        if seq_bin_n[i] == "1":
            one_count += 1
            if one_count == 2:
                ans.append(zero_count)
                one_count = 1
                zero_count = 0
        elif one_count == 1 and seq_bin_n[i] == "0":
            zero_count += 1

    return max(ans)
