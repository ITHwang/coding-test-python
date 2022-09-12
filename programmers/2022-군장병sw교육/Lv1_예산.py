def solution(d, budget):
    d.sort()
    cnt = 0
    for i in range(len(d)):
        if d[i] <= budget:
            budget -= d[i]
            cnt += 1
        else:
            break
    return cnt
