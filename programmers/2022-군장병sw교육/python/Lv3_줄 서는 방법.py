import math


def solution(n, k):
    arr = [i for i in range(1, n + 1)]
    answer = []
    for j in reversed(range(1, n)):
        fact = math.factorial(j)
        idx = (k - 1) // fact
        answer.append(arr[idx])
        arr.pop(idx)
        k %= fact
    answer.append(arr[0])
    return answer
