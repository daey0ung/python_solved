import sys
input = sys.stdin.readline
N = int(input())
A = []
for i in range(N):
    A.append(list(input().split()))

A.sort(key=lambda x: int(x[0]))
for i in A:
    print(*i)