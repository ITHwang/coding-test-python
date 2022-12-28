import heapq


def solution(operations):
    min_q, max_q = [], []
    for oper in operations:
        cmd, num = oper.split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)
        else:
            if num == 1:
                if not max_q: continue
                max_num = -heapq.heappop(max_q)
                min_q.remove(max_num)
            else:
                if not min_q: continue
                min_num = heapq.heappop(min_q)
                max_q.remove(-min_num)
    if max_q: return [-heapq.heappop(max_q), heapq.heappop(min_q)]
    else: return [0, 0]