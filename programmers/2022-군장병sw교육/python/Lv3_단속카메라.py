def solution(routes):
    routes.sort(key=lambda x: x[1])
    cnt = 1
    curr_cam = routes[0][1]
    for route in routes[1:]:
        if curr_cam not in range(route[0], route[1] + 1):
            cnt += 1
            curr_cam = route[1]
    return cnt
