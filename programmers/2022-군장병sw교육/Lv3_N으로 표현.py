def solution(n, number):
    d = [set() for _ in range(9)]
    d[1].add(n)
    for i in range(2, 9):
        d[i].add(int(str(n) * i))
        for j in range(i // 2 + 1):
            for k in d[j]:
                for m in d[i - j]:
                    d[i].add(k + m)
                    d[i].add(k - m)
                    d[i].add(m - k)
                    d[i].add(m * k)
                    if k != 0: d[i].add(m // k)
                    if m != 0: d[i].add(k // m)
        if number in d[i]: return i
    return -1