def solution(w, h):
    gcd = 0
    for i in reversed(range(2, w + 1)):
        if w % i == 0 and h % i == 0:
            gcd = i
            break
    else:
        return w * h - (w + h - 1)
    w_small = w / gcd
    h_small = h / gcd
    return w * h - gcd * (w_small + h_small - 1)
