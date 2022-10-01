def solution(tree):
    d = [[0] * (i+1) for i in range(len(tree))]
    d[0] = tree[0]
    for i in range(1, len(d)):
        for j in range(len(d[i])):
            if j == 0: d[i][j] = tree[i][j] + d[i-1][j]
            elif j == len(d[i])-1: d[i][j] = tree[i][j] + d[i-1][-1]
            else: d[i][j] = tree[i][j] + max(d[i-1][j-1], d[i-1][j])
    return max(d[-1]))