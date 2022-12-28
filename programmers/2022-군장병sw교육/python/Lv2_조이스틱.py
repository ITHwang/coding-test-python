def change(alphabet):
    return min(ord(alphabet) - 65, ord('Z') - ord(alphabet) + 1)


def solution(name):
    move = len(name) - 1
    cnt = 0
    for i, ch in enumerate(name):
        cnt += change(ch)
        if ch != 'A': continue
        end = i + 1
        while end < len(name) and name[end] == 'A':
            end += 1
        if i == 0: right = 0
        else: right = i - 1
        left = len(name) - end
        move = min(move, left + right + min(left, right))
    return cnt + move
