chk = [1] * 1000001


def solution(n):
    for i in range(2, n // 2 + 1):
        mul = 2
        while i * mul <= n:
            chk[i * mul] = 0
            mul += 1
    return len(
        [idx for idx, isTrue in enumerate(chk[:n + 1]) if idx >= 2 and isTrue])
