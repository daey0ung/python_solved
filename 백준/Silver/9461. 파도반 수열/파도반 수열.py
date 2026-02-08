import sys
input = sys.stdin.readline

# DP 테이블 초기화: N의 최대 범위(100)만큼 0으로 채움
P = [0] * 101

# 초기 상태 설정: P[1]~P[3]은 모두 1
P[1:4] = [1, 1, 1]

# 보텀업(Bottom-up) DP: 점화식을 이용하여 4부터 100까지 미리 계산
for i in  range(4,101):
    P[i] = P[i-2] + P[i-3]

T = int(input())

for _ in range(T):
    N = int(input())
    print(P[N])