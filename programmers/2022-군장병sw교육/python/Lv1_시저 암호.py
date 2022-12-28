def push_asc(asc, n):
    pushed = asc + n
    if 65 <= asc and asc <= 90 and pushed > 90:
        pushed = pushed % 90 + 64
    if 97 <= asc and asc <= 122 and pushed > 122:
        pushed = pushed % 122 + 96
    return chr(pushed)


def solution(strs, n):
    ans = ''
    for s in strs:
        asc = ord(s)
        if asc == 32: ans += s
        else: ans += push_asc(asc, n)
    return ans