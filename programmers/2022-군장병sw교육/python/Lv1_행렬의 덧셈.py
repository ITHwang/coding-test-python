def pointwise_sum(a, b):
    return [e1 + e2 for e1, e2 in zip(a, b)]


def solution(arr1, arr2):
    return [pointwise_sum(row1, row2) for row1, row2 in zip(arr1, arr2)]
