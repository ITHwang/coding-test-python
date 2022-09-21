def solution(n):
    cnt = 0
    stk = []
    for i in range(1, n // 2 + 1):
        stk.append((i, i))
    while stk:
        last_num, acc = stk.pop()
        sum_ = last_num + 1 + acc
        if sum_ == n: cnt += 1
        elif sum_ < n: stk.append((last_num + 1, sum_))
    return cnt + 1