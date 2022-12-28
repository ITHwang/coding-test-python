from collections import deque


def is_possible(x, y, direct):
    if direct == 'U' and y == 5: return False
    elif direct == 'D' and y == -5: return False
    elif direct == 'R' and x == 5: return False
    elif direct == 'L' and x == -5: return False
    else: return True


def solution(dirs):
    answer = 0
    visited = []
    curr_x, curr_y = 0, 0
    q = deque(dirs)
    while q:
        direct = q.popleft()
        if not is_possible(curr_x, curr_y, direct): continue
        next_x, next_y = curr_x, curr_y
        if direct == 'U': next_y += 1
        elif direct == 'D': next_y -= 1
        elif direct == 'R': next_x += 1
        else: next_x -= 1
        if (curr_x, curr_y, next_x, next_y) not in visited:
            visited.append((curr_x, curr_y, next_x, next_y))
            visited.append((next_x, next_y, curr_x, curr_y))
            answer += 1
        curr_x, curr_y = next_x, next_y
    return answer