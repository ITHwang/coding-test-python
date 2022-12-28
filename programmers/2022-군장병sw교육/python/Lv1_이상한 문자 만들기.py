def change_chars(word):
    changed = ''
    for i, c in enumerate(word):
        c = c.upper() if i % 2 == 0 else c.lower()
        changed += c
    return changed


def solution(s):
    words = s.split(' ')
    return ' '.join([change_chars(word) for word in words])
