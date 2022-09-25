def solution(land):
    d = [[0] * 4 for _ in land]
    d[0] = land[0]
    for i in range(1, len(land)):
        for j in range(4):
            a, b, c = [k for k in range(4) if k != j]
            d[i][j] = land[i][j] + max(d[i - 1][a], d[i - 1][b], d[i - 1][c])
    return max(d[-1])