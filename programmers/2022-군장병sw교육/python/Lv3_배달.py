import heapq


def solution(n, paths, k):
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))
    q = []
    heapq.heappush(q, (0, 1))
    min_dist = [INF] * (n + 1)
    min_dist[1] = 0
    while q:
        curr_dist, curr_node = heapq.heappop(q)
        if curr_dist > min_dist[curr_node]: continue
        for next_node, next_dist in graph[curr_node]:
            cost = curr_dist + next_dist
            if cost < min_dist[next_node]:
                min_dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return sum([dist <= k for dist in min_dist[1:]])
