def solution(n, stations, w):
    cnt = 0
    unreached = []
    curr_node = 1

    for station in stations:
        min_node, max_node = station - w, station + w
        if min_node > curr_node: unreached.append((curr_node, min_node - 1))
        curr_node = max_node + 1
    if curr_node < n + 1: unreached.append((curr_node, n))

    for start_node, end_node in unreached:
        unreached_length = end_node - start_node + 1
        if unreached_length % (2 * w + 1) == 0:
            cnt += unreached_length // (2 * w + 1)
        else:
            cnt += (unreached_length // (2 * w + 1)) + 1
    return cnt