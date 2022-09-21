def cnt_ones(num):
    cnt = 0
    while num != 0:
        if num % 2 != 0: cnt += 1
        num //= 2
    return cnt


def solution(n):
    ones = cnt_ones(n)
    result = n + 1
    while True:
        if ones == cnt_ones(result):
            return result
        result += 1
