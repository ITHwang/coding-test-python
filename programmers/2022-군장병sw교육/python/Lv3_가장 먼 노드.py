import heapq


def solution(n, vertex):
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    for src, dst in vertex:
        graph[src].append(dst)
        graph[dst].append(src)
    min_dist = [INF] * (n + 1)
    min_dist[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        curr_dist, curr_node = heapq.heappop(q)
        if curr_dist > min_dist[curr_node]: continue
        for next_node in graph[curr_node]:
            cost = min_dist[curr_node] + 1
            if cost < min_dist[next_node]:
                min_dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    max_dist = max(min_dist[1:])
    return sum([dist == max_dist for dist in min_dist[1:]])
