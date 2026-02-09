N,M= map(int, input().split())
list_10813 = [i+1 for i in range(N)]
for _ in range(M):
    i,j = map(int, input().split())
    list_10813[i-1] , list_10813[j-1] = list_10813[j-1], list_10813[i-1]

print(*list_10813)