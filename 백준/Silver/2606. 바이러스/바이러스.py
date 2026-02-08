from collections import deque
import sys
input = sys.stdin.readline

# BFS(너비 우선 탐색 알고리즘) 사용

# 컴퓨터 수 입력받기
N = int(input())

# 컴퓨터 쌍의 수 입력 받기
V = int(input())

# 각 컴퓨터에 연결된 번호들을 저장하는 2차원 리스트
graph = [[] for _ in range(N+1)]

# 바이러스 감염여부를 파악하는 리스트 / 0: 미감염, 1:감염
virus = [0] * (N+1)

# 컴퓨터에 연결된 번호들을 저장하는 반복문
for i in range(V):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

virus[1] = 1
# 1번부터 감염시작하므로 1로 시작
Q = deque([1])
while Q:
    x = Q.popleft()
    for i in graph[x]: # x에 연결된 컴퓨터를 불러옴
        if virus[i] == 0: # 연결된 컴퓨터가 바이러스에 걸렸다는걸 몰랐다면
            Q.append(i) # 검사 deque에 추가
            virus[i] = 1 # 바이러스 감염으로 수정

# 1번은 제외하므로 -1
print(sum(virus)-1)