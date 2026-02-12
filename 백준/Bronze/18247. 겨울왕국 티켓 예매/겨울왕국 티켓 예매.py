N = int(input())

for _ in range(N):
    y, x = map(int, input().split())

    if x>=4 and y>=12:
        print(11*x+4)
    else:
        print(-1)