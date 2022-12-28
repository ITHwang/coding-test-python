import heapq

def solution(genres, plays):
    answer = []
    dic = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic: 
            dic[genre] = []
        heapq.heappush(dic[genre], (-play, i))
    genres = sorted(dic.items(), key=lambda x: sum([minus_play for minus_play, idx in x[1]]))
    for genre, musics in genres:
        if len(musics) == 1: 
            answer.append(musics[0][1])
            continue
        for _ in range(2): 
            answer.append(heapq.heappop(musics)[1])
    return answer