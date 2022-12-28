def solution(arr, divisor):
    divided = [e for e in arr if e % divisor == 0]
    return sorted(divided) if divided else [-1]
