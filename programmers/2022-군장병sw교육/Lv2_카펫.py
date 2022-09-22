def solution(brn, ylw):
    all = brn + ylw
    for w in reversed(range(all + 1)):
        if all % w != 0: continue
        h = all / w
        y = (w - 2) * (h - 2)
        b = all - y
        if b == brn and y == ylw: return w, h
