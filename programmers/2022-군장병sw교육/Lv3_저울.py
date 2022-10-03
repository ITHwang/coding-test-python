def solution(weights):
    weights.sort()
    acc = weights[0]
    if acc != 1: return 1
    for i in range(1, len(weights)):
        if acc + 1 < weights[i]: return acc + 1
        acc += weights[i]
    return acc + 1