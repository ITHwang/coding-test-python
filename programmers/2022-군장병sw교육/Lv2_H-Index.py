def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    for i, citation in enumerate(citations):
        if citation > n: continue
# not yet