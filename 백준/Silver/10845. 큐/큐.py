import sys
from collections import deque
input = sys.stdin.readline

stack = deque()
N = int(input())

for _ in range(N):
    A = list(input().split())
    # print(A[0])
    if A[0] == 'push':
        stack.append(A[1])
    elif A[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.popleft())
    elif A[0] == 'size':
        print(len(stack))
    elif A[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif A[0] == 'front':
        if len(stack) != 0:
            print(stack[0])
        else:
            print(-1)
    elif A[0] == 'back':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    # print(stack)