def solution(s):
    isEven = len(s) % 2 == 0
    half = len(s) // 2
    return s[half-1:half+1] if isEven else s[half]