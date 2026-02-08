import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int,input().split()))
L.sort()
answer = 0
current = 0
for i in L:
    current += i
    answer += current

print(answer)