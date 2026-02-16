N, M = map(int, input().split())

S = {}
for _ in range(N):
    strN = input()
    S[strN] = 1

cnt = 0
for _ in range(M):
    strM = input()
    if strM in S:
        cnt += 1

print(cnt)