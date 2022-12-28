def jaden(word):
    return ''.join([ch.upper() if i == 0 else ch for i, ch in enumerate(word)])


def solution(string):
    words = [jaden(word.lower()) for word in string.split(' ')]
    return ' '.join(words)

    