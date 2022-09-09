def solution(string):
    symbol = None
    if string[0] == '+' or string[1] == '-':
        string = string[1:]
        symbol = string[0]
    return -int(string) if symbol == '-' else int(string)