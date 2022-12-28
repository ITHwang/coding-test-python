def solution(a, b):
    a, b = a, b if a < b else b, a
    return sum(list(range(a, b + 1)))
