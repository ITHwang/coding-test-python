def solution(string):
    return ''.join(
        [chr(i) for i in sorted([ord(c) for c in string], reverse=True)])
