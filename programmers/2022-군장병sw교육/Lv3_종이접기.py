import copy


def solution(n):
    arr = [0]
    for i in range(2, n + 1):
        tmp = []
        insert_ch = 0
        for a in arr:
            tmp.append(insert_ch)
            tmp.append(a)
            insert_ch = 0 if insert_ch == 1 else 1
        tmp.append(insert_ch)
        arr = copy.deepcopy(tmp)
    return arr
