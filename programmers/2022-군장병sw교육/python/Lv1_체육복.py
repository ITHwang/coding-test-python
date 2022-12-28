def solution(n, lost, reserve):
    uniforms = [1] * (n + 2)
    for l in lost:
        uniforms[l] = 0
    for r in reserve:
        if r in lost: uniforms[r] = 1
        else: uniforms[r] = 2
    for i in range(1, n + 1):
        if uniforms[i] == 0:
            if uniforms[i + 1] == 2:
                uniforms[i] = 1
                uniforms[i + 1] = 1
            elif uniforms[i - 1] == 2:
                uniforms[i] = 1
                uniforms[i - 1] = 1
    return len([i for i in uniforms[1:n + 1] if i == 1 or i == 2])
