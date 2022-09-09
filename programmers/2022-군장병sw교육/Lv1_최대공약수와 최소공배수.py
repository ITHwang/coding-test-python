def getLcm(small, big):
    for i in range(big, small*big+1):
        if i % small == 0 and i % big == 0:
            return i
def getGcm(small, big):
    for i in reversed(range(1, small+1)):
        if small % i == 0 and big % i == 0:
            return i
def solution(n, m):
    if n < m:
        small = n
        big = m
    else:
        small = m
        big = n
    gcm = getGcm(small, big)
    lcm = getLcm(small, big)
    return gcm , lcm
    