def solution(n, times):
    times.sort()
    left, right = 0, times[-1] * n
    min_time = times[-1] * n
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
            if cnt >= n:
                min_time = min(min_time, mid)
                right = mid - 1
                break
        else:
            left = mid + 1
    return min_time