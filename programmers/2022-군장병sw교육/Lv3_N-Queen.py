def f(h, s, bs, col):
    cnt = 0
    n = len(h)
    if col == n: return 1
    for i in range(n):
        if h[i] or s[col + i] or bs[col - i + n - 1]: continue
        h[i] = s[col + i] = bs[col - i + n - 1] = True
        cnt += f(h, s, bs, col + 1)
        h[i] = s[col + i] = bs[col - i + n - 1] = False
    return cnt


def solution(n):
    h = [False] * n
    s = [False] * (2 * (n - 1) + 1)
    bs = [False] * (2 * (n - 1) + 1)
    return f(h, s, bs, 0)