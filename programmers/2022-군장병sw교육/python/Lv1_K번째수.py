def solution(arr, cmds):
    found_elements = []
    for i, j, k in cmds:
        found_elements.append(sorted(arr[i - 1:j])[k - 1])
    return found_elements