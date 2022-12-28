def solution(n):
    ints = [s for s in str(n)]
    return int(''.join(sorted(ints, reverse=True)))