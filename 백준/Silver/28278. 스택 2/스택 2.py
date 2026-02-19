import sys
input = sys.stdin.readline
T = int(input())

stack = []
for _ in range(T):
    A = list(map(int, input().split()))
    stack_length = len(stack)
    if A[0] == 1:
        stack.append(A[1])
    elif A[0] == 2:
        if stack_length:
            print(stack.pop())  
        else:
            print(-1)
    elif A[0] == 3:
        print(stack_length)
    elif A[0] == 4:
        if stack_length:
            print(0)
        else:
            print(1)
    elif A[0] == 5:
        if stack_length:
            print(stack[-1])
        else:
            print(-1)