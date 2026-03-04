import sys
input = sys.stdin.readline

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

def w(a,b,c):
    if a<=0 or b<=0 or c <= 0: # 1번 조건
        return 1
    if a>20 or b>20 or c> 20: # 2번 조건
        return w(20,20,20)
    if dp[a][b][c] != 0: # 기록된 값이라면(20이상의 값이 들어오면 오류가 생기므로 2번 조건 이후에 실행되게 수정)
        return dp[a][b][c]
    if a<b<c: # 3번 조건
        dp[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
    else: # 모두 아닌 경우
        dp[a][b][c] = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)

    return dp[a][b][c]

while True:
    a,b,c = map(int, input().split())
    if a==b==c==-1: # 종료 조건
        break

    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')