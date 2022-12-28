def solution(progresses, speeds):
    days = []
    for progress, speed in zip(progresses, speeds):
        remaining_time = 100 - progress
        if remaining_time % speed == 0: days.append(remaining_time // speed)
        else: days.append(remaining_time // speed + 1)
    for i in range(1, len(days)):
        if days[i - 1] > days[i]: days[i] = days[i - 1]
    cnts = [0] * 101
    for day in days:
        cnts[day] += 1
    return [cnt for cnt in cnts if cnt != 0]