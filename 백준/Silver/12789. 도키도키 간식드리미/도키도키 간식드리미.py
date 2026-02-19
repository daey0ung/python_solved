import sys
input = sys.stdin.readline
T = int(input())

arr = list(map(int, input().split()))
stack = []
n = 1
i = 0
while i<T:
    if arr[i] == n:
        n += 1 
    else:
        stack.append(arr[i])
    i += 1
    while stack and stack[-1] == n:
        stack.pop()
        n += 1

if stack:
    print('Sad')
else:
    print('Nice')
