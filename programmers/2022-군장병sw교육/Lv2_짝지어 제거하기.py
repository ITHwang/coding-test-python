def solution(string):
    stk = []
    for s in string:
        if not stk: stk.append(s)
        elif stk[-1] == s: stk.pop()
        else: stk.append(s)
    return 0 if stk else 1