max_num = 50000
prime_num_chk = [1] * (max_num + 1)
prime_num_chk[0] = 0
prime_num_chk[1] = 0
for i in range(2, max_num // 2 + 1):
    mul = 2
    while i * mul <= max_num:
        prime_num_chk[i * mul] = 0
        mul += 1
prime_nums = [idx for idx, chk in enumerate(prime_num_chk) if chk == 1]


def solution(nums):
    global prime_nums
    n = len(nums)
    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] in prime_nums: cnt += 1
    return cnt
