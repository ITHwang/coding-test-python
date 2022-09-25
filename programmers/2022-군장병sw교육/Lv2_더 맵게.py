import heapq


def solution(scoville, k):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] >= k:
        if len(scoville) == 1: return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a + 2 * b
        heapq.heappush(scoville, c)
        cnt += 1
    return cnt
