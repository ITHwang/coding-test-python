def solution(baseball):
    cnt = 0
    for i in range(123, 988):
        cand = str(i)
        if cand[1] == '0' or cand[2] == '0': continue
        if cand[0] == cand[1] or cand[1] == cand[2] or cand[0] == cand[2]:
            continue
        for query, strike, ball in baseball:
            cand_strike = 0
            cand_ball = 0
            query = str(query)
            for j in range(3):
                for k in range(3):
                    if j == k:
                        if cand[j] == query[k]: cand_strike += 1
                    else:
                        if cand[j] == query[k]: cand_ball += 1
            if strike != cand_strike or ball != cand_ball: break
        else: cnt += 1
    return cnt
