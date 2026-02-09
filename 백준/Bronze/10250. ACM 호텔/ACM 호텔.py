N = int(input())
for i in range(N):
    a = input().split()
    H = int(a[2])%int(a[0])
    if H ==0:
        H=a[0]
        W = int(a[2])//int(a[0])
    else:
        W = int(a[2])//int(a[0])+1
    if len(str(W)) == 1:
        W = '0'+ str(W)
    print(H,W, sep='')