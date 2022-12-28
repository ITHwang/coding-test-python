import heapq


def solution(n, costs):
    graph = [[] for _ in range(n)]
    for cost in costs:
        graph[cost[0]].append((cost[1], cost[2]))
        graph[cost[1]].append((cost[0], cost[2]))

    visited = [False] * n
    visited[0] = True
    q = []
    total_cost = 0
    for next_node, cost in graph[0]:
        heapq.heappush(q, (cost, next_node))
    while q:
        cost, curr_node = heapq.heappop(q)
        if not visited[curr_node]:
            visited[curr_node] = True
            total_cost += cost
            for next_node, cost in graph[curr_node]:
                heapq.heappush(q, (cost, next_node))
    return total_cost
