def solution(works, n):
    if sum(works) <= n: return 0
    mean = sum(works) // len(works)
    works.sort(reverse=True)
    for i in range(len(works)):
        if works[i] > mean and n > 0:
            gap = works[i] - mean
            works[i] -= gap
            n -= gap
            if n < 0:
                works[i] -= n
                n = 0
    if n == 0: return sum([w*w for w in works])
    k = n // len(works)
    n -= k * len(works)
    for j in range(len(works)):
        works[j] -= k
    while n > 0:
        for j in range(len(works)):
            if n > 0 and works[j] > 0:
                works[j] -= 1
                n -= 1
    return sum([w*w for w in works])
# not yet