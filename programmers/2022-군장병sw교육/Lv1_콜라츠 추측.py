def solution(n):
    cnt = 0
    while n != 1:
        isEven = n % 2 == 0
        n = n // 2 if isEven else n * 3 + 1
        cnt += 1
        if cnt == 500:
            cnt = -1
            break
    return cnt