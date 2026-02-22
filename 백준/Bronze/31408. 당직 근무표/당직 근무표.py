import sys
input = sys.stdin.readline

N = int(input())
num_count = {}
for i in map(int,input().split()):
    if i in num_count:
        num_count[i] += 1
    else:
        num_count[i] = 1

num_mode = max(num_count.values())

if num_mode > (N+1)//2:
    print('NO')
else:
    print('YES')