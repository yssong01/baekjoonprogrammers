# 체스 피스 : 총 16개,
# 정상 : 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
chess = [1, 1, 2, 2, 2, 8]

#소유중인 (찾은) 피스
#get = [0, 1, 2, 2, 2, 7]
get = list( map(int, input().split()) )

for c, g in zip(chess, get): # zip()으로, 두 목록(chess, get)을 쌍으로 묶기
    print(c - g, end=' ')