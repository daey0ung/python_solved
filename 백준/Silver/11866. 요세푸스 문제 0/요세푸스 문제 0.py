import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
A = deque()
answer = []

for i in range(N):
    A.append(i+1)


for _ in range(N):
    A.rotate(-(K-1))
    answer.append(A.popleft())

print(f'<{", ".join(map(str, answer))}>')