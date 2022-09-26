import functools


def compare(x, y):
    x, y = ''.join(x), ''.join(y)
    if x > y: return 1
    elif x < y: return -1
    else: return 0


def solution(tickets):
    stk = [('ICN', tickets, [])]
    answers = []
    while stk:
        dst, tickets, visited = stk.pop()
        if not tickets:
            answers.append(visited + [dst])
            continue
        for i, ticket in enumerate(tickets):
            if ticket[0] == dst:
                next_dst = ticket[1]
                remained_ticket = tickets[:i] + tickets[i + 1:]
                next_visited = visited + [ticket[0]]
                stk.append((next_dst, remained_ticket, next_visited))
    answers.sort(key=functools.cmp_to_key(compare))
    return answers[0]
