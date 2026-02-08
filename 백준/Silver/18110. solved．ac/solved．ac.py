import sys
input = sys.stdin.readline

N = int(input())

if N == 0:
    print(0)
    exit()

A = []
for i in range(N):
    A.append(int(input()))
A.sort()

drop_N = int(N*0.15+0.5)
sum_A = 0
cnt = 0

for i in range(drop_N, len(A)-drop_N):
    sum_A += A[i]
    cnt += 1

print(int((sum_A/cnt)+0.5))