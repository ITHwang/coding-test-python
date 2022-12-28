def solution(n):
    mapping = [4, 1, 2]
    nums = []
    while n != 0:
        remainder = n % 3
        nums.append(str(mapping[remainder]))
        n //= 3
        if remainder == 0:
            n -= 1
    return ''.join(reversed(nums))