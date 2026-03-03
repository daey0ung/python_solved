# 중복 조합
N, M = map(int, input().split())
array = [i for i in range(1,N+1)]

def backtrack(idx, arr):
	if len(arr) == M:
		print(*arr, sep=' ',)
		return
	
	for i in range(idx, len(array)):
		backtrack(i, arr + [array[i]])

backtrack(0, [])