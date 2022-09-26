def solution(nums):
    n_pick = int(len(nums) / 2)
    nums = sorted(list(set(nums)))
    if n_pick >= len(nums): return len(nums)
    else: return n_pick