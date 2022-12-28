def solution(string):
    if len(string) != 4 and len(string) != 6: return False
    return all(48 <= ord(c) and ord(c) <= 57 for c in string)