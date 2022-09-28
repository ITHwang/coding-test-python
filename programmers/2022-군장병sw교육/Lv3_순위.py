class Node:

    def __init__(self):
        self.parents = []
        self.children = []


def solution(n, results):
    cnt = 0

    nodes = [Node() for _ in range(n + 1)]
    for i in range(len(results)):
        nodes[results[i][0]].children.append(results[i][1])
        nodes[results[i][1]].parents.append(results[i][0])

    for j in range(1, n + 1):
        connected = [0] * (n + 1)
        connected[j] = 1
        stk = [j]
        while stk:
            parent_idx = stk.pop()
            for child_idx in nodes[parent_idx].children:
                if not connected[child_idx]:
                    connected[child_idx] = 1
                    stk.append(child_idx)
        stk = [j]
        while stk:
            child_idx = stk.pop()
            for parent_idx in nodes[child_idx].parents:
                if not connected[parent_idx]:
                    connected[parent_idx] = 1
                    stk.append(parent_idx)
        if all(connected[1:]): cnt += 1

    return cnt