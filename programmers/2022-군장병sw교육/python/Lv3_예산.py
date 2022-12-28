import heapq


def cal_budget(mid, budgets):
    return sum([budget if budget <= mid else mid for budget in budgets])


def solution(budgets, total_budget):
    total_requested_budget = sum(budgets)
    if total_requested_budget < total_budget: return max(budgets)
    start = total_budget // len(budgets)
    end = max(budgets)
    q = []
    while start <= end:
        mid = (start + end) // 2
        curr_budget = cal_budget(mid, budgets)
        if curr_budget <= total_budget:
            heapq.heappush(q, (-curr_budget, mid))
            start = mid + 1
        elif curr_budget > total_budget:
            end = mid - 1
        else:
            return mid
    return heapq.heappop(q)[1]