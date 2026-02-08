import sys
input = sys.stdin.readline

stack = []
N = int(input())

for _ in range(N):
    A = list(input().split())

    if A[0] == 'push':
        stack.append(A[1])
    elif A[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif A[0] == 'size':
        print(len(stack))
    elif A[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif A[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)