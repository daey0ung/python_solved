import sys
input = sys.stdin.readline
N=int(input())
H, W= [], []
for i in range(N):
    x, y = map(int, input().split())
    W.append(x)
    H.append(y)
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        if H[i] < H[j] and W[i] < W[j]:
            cnt +=1
            
    print(cnt+1, sep=' ')