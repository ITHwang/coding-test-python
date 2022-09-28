def solution(a, b):
    score = 0
    a, b = sorted(a), sorted(b)
    while b:
        if b[0] <= a[0]:
            a.pop()
            b.pop(0)
        else:
            score += 1
            a.pop(0)
            b.pop(0)
    return score