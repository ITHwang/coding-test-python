def solution(heights):
    answer = []
    for i in range(len(heights)):
        for j in reversed(range(i)):
            if heights[i] < heights[j]:
                answer.append(j + 1)
                break
        else: answer.append(0)
    return answer