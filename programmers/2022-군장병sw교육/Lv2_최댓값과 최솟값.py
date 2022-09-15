def solution(string):
    nums = list(map(int, string.split()))
    nums.sort()
    return f'{nums[0]} {nums[-1]}'