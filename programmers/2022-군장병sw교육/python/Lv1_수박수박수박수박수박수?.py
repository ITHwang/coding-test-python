def solution(n):
    res = '수박' * (n // 2)
    if n % 2 == 1: res += '수'
    return res