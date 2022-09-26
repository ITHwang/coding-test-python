import functools


def f(x, y):
    x_str, y_str = str(x), str(y)
    a = int(x_str + y_str)
    b = int(y_str + x_str)
    if a > b: return -1
    elif a < b: return 1
    else: return 0


def solution(numbers):
    numbers.sort(key=functools.cmp_to_key(f))
    return str(int(''.join([str(number) for number in numbers])))
