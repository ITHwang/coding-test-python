import math


def solution(n):
    sq = math.sqrt(n)
    isTrue = int(sq) == sq
    return (sq + 1) * (sq + 1) if isTrue else -1
