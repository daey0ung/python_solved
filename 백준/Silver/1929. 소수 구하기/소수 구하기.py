import sys
input = sys.stdin.readline

M,N = map(int,input().split())
A = [False,False] + [True]*(N-1)
primes=[]

for i in range(2,N+1):
  if A[i]:
    primes.append(i)
    for j in range(2*i, N+1, i):
        A[j] = False

for i in range(M,N+1):
    if A[i]:
        print(i)