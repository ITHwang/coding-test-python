import heapq
from collections import deque


def solution(jobs):
    total = len(jobs)
    jobs = deque(
        sorted([(job[1], job[0]) for job in jobs], key=lambda x: (x[1], x[0])))
    scheduled = []
    heapq.heappush(scheduled, jobs.popleft())
    now, acc = 0, 0
    while scheduled:
        duration, start = heapq.heappop(scheduled)
        now = max(start + duration, now + duration)
        acc += now - start
        while jobs and jobs[0][1] <= now:
            heapq.heappush(scheduled, jobs.popleft())
        if jobs and not scheduled:
            heapq.heappush(scheduled, jobs.popleft())
    return acc // total
