def filter_skill(tree, skill):
    return ''.join([ch for ch in tree if ch in skill])


def solution(skill, trees):
    trees = [filter_skill(tree, skill) for tree in trees]
    cnt = 0
    for tree in trees:
        if not tree: cnt += 1
        elif tree == skill[:len(tree)]: cnt += 1
    return cnt
