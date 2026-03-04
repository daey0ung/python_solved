import sys
input = sys.stdin.readline


N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]
min_result = int(1e9)
visited = [False] * N

def dfs(count, idx):
	global min_result
	if count == N//2: # 인원 배분이 완료되면
		start = 0
		link = 0
		
		for i in range(N):
			for j in range(N):
				if visited[i] and visited[j]: # start팀 능력치 더하기
					start += status[i][j]
				elif not visited[i] and not visited[j]: # link팀 능력치 더하기
					link += status[i][j]
		
		min_result = min(min_result, abs(start-link))
		return
	
    # 인원 배분하기
	for i in range(idx, N):
		if not visited[i]:
			visited[i] = True
			dfs(count+1, i+1)
			visited[i] = False

dfs(0, 0)
print(min_result)