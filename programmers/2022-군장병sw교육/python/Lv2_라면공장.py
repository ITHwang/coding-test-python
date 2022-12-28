import heapq


def solution(stock, dates, supplies, k):
    que = []
    s = 0
    cnt = 0
    while stock < k:
        for i in range(s, len(dates)):
            if stock >= dates[i]:
                heapq.heappush(que, (-supplies[i], supplies[i]))
                s = i + 1
            else:
                break
        stock += heapq.heappop(que)[1]
        cnt += 1
    return cnt
