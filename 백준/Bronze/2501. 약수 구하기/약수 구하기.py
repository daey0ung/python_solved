import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 1

for i in range(1, N+1):
    if N % i == 0:
        if cnt == K:
            print(i)
            sys.exit()
        cnt += 1

print(0)