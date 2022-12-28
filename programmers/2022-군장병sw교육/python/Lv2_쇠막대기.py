def solution(arrangement):
    cnt = 0
    stk = []
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stk.append(arrangement[i])
        else:
            if arrangement[i - 1] == '(':
                stk.pop()
                cnt += len(stk)
            else:
                stk.pop()
                cnt += 1
    return cnt