def solution(arr):
    curr = -1
    result_arr = []
    for e in arr:
        if e == curr: continue
        result_arr.append(e)
        curr = e
    return result_arr
