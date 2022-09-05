def solution(s):
    s = s.lower()
    num_p = 0
    num_y = 0
    for c in s:
        if c == 'p': num_p += 1
        elif c == 'y': num_y += 1
    return num_p == num_y