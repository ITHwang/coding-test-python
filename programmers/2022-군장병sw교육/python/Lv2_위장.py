import math

def solution(clothes):
    dic = {}
    for cloth in clothes:
        if cloth[1] in dic: dic[cloth[1]].append(cloth[0])
        else: dic[cloth[1]] = [cloth[0]]
    nums = [len(v) + 1 for k, v in dic.items()]
    return math.prod(nums) - 1 