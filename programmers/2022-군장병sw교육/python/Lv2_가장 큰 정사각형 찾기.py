def solution(board):
    row = len(board)
    col = len(board[0])
    d = [[0] * 1001 for _ in range(1001)]
    max_ = 0
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if board[i - 1][j - 1]:
                d[i][j] = board[i - 1][j - 1] + min(d[i - 1][j], d[i][j - 1],
                                                    d[i - 1][j - 1])
                max_ = max(max_, d[i][j])
    return max_ * max_
