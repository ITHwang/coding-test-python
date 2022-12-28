def solution(n, money):
    money.sort()
    d = [0] * (n + 1)
    d[0] = 1
    for m in money:
        for i in range(m, n + 1):
            d[i] = (d[i] + d[i - m]) % 10000007
    return d[n]
