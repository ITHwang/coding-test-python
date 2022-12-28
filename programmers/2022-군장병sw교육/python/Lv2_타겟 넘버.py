def solution(nums, tgt):
    cnt = 0
    nums.sort(reverse=True)
    # idx, acc
    stk = [(1, -nums[0]), (1, nums[0])]
    while stk:
        idx, acc = stk.pop()
        plus = acc + nums[idx]
        minus = acc - nums[idx]
        if idx == len(nums) - 1:
            if plus == tgt: cnt += 1
            if minus == tgt: cnt += 1
            continue
        stk.append((idx + 1, plus))
        stk.append((idx + 1, minus))
    return cnt