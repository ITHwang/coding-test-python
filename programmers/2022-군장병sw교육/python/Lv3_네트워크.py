def solution(n, connections):
    visited = [0] * n
    cnt = 0
    while not all(visited):
        i = visited.index(0)
        stk = [i]
        while stk:
            j = stk.pop()
            visited[j] = 1
            for k in range(len(connections[j])):
                if connections[j][k] and not visited[k]: stk.append(k)
        cnt += 1
    return cnt