def sum_(n):
    return sum([int(e) for e in str(n)])


def solution(n):
    return n % sum_(n) == 0
