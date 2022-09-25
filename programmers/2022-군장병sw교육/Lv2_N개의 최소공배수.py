import math

def solution(arr):
    for i in range(max(arr), math.prod(arr)+1):
        if all([i % elem == 0 for elem in arr]): return i
    else: return math.prod(arr)