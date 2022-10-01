from collections import deque

def chk(src, dst):
    return sum([a == b for a, b in zip(src, dst)]) == len(src) - 1

def solution(begin, target, words):
    q = deque()
    if target not in words: return 0
    for i, word in enumerate(words):
        if chk(begin, word): 
            if word == target: return 1 
            q.append((1, word, words[:i]+words[i+1:]))
    while q:
        cnt, begin, remained_words = q.popleft()
        if begin == target: return cnt
        for i, word in enumerate(remained_words):
            if chk(begin, word): 
                q.append((cnt+1, word, remained_words[:i]+remained_words[i+1:]))
    return 0 