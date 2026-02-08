import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list((map(int,input().split())))

# 누적합 리스트 생성
S = [0]
for i in range(len(A)):
    S.append(S[-1]+A[i])

for _ in range(M):
    i, j = map(int, input().split())
    print(S[j]- S[i-1])