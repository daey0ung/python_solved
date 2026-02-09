import sys

input = sys.stdin.readline
N = int(input())

cnt = [0] * 10001

for _ in range(N):
    x = int(input())
    cnt[x] += 1

for i in range(10001):
    if cnt[i]:
        for j in range(cnt[i]):
            print(i)