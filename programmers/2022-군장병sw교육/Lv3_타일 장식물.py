def solution(n):
    # 4, 6, 10, 16, 26...
    d = [0] * (n + 1)
    d[1] = 4
    d[2] = 6
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[n]