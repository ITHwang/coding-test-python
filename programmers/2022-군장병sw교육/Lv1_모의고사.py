def solution(ans):
    first = [1, 2, 3, 4, 5] * 2000
    second = ([2] + [1, 2, 3, 2, 4, 2, 5, 2] * (10000 // 8 + 1))[:10000]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000
    first_right = [a for a, b in zip(first[:len(ans)], ans) if a == b]
    second_right = [a for a, b in zip(second[:len(ans)], ans) if a == b]
    third_right = [a for a, b in zip(third[:len(ans)], ans) if a == b]
    num_ans = [len(first_right), len(second_right), len(third_right)]
    max_ = max(num_ans)
    max_stu = [i + 1 for i in range(len(num_ans)) if num_ans[i] == max_]
    max_stu.sort()
    return max_stu
