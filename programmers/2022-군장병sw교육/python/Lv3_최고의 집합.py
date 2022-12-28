def solution(n, s):
    if s // n == 0: return [-1]
    arr = [s // n] * n
    for i in range(s % n):
        arr[-1 - i] += 1
    return arr