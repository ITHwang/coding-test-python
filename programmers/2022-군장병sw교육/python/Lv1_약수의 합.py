def solution(n):
    res = 0
    for i in range(1, n + 1):
        if i * i == n:
            res += i
            break
        elif i * i > n:
            break
        if n % i == 0:
            res += i
            res += n / i
    return res
