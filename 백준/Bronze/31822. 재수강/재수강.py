import sys
input = sys.stdin.readline

N = input().strip()
M = int(input())
cnt = 0

for _ in range(M):
    A = input().strip()
    if A[:5] == N[:5]:
        cnt += 1

print(cnt)