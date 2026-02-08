N = int(input())

A = list(map(int, input().split()))
A += [0] * (5 - len(A))

if A[0]>A[2]:
    a = (A[0]-A[2])*508
else:
    a = (A[2]-A[0])*108

if A[1] > A[3]:
    b = (A[1]-A[3])*212
else:
    b = (A[3]-A[1])*305

c = A[4] * 707

answer = (a+b+c) * 4763
print(answer)