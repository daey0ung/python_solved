import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    A = int(input())
    if A == 0:
        stack.pop()
    else:
        stack.append(A)

print(sum(stack))