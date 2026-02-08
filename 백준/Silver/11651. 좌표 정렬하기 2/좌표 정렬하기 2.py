import sys
input = sys.stdin.readline
N = int(input())
A = []
for _ in range(N):
    A.append(tuple(map(int, input().split())))

A.sort(key=lambda x: (x[1], x[0]))

for x,y in A:
    print(x,y)