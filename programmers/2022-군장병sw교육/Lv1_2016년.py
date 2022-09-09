days_of_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def solution(a, b):
    days = sum(days_of_month[:a]) - 1
    days -= days_of_month[a-1] - b
    idx = (5 + days) % 7
    return days_of_week[idx]