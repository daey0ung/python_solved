import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

dq = deque(i for i in range(1,T+1))

arr = list(map(int,input().split()))
for _ in range(T):
    idx = dq.popleft()
    print(idx, end=' ')
    if arr[idx-1]>0:
        dq.rotate(-(arr[idx-1]-1))
    else:
        dq.rotate(-arr[idx-1])