N = int(input())
array = [list(map(int, input().split())) for _ in range(N)] # 입력 배열
dp = [[0]*N for _ in range(N)] # 결과 계산 배열

dp[0] = array[0] # 초기값 설정
for i in range(1,N):
    for j in range(i+1):
        if j ==0: # 첫번째는 경우
            dp[i][j] = dp[i-1][j] + array[i][j]
        elif j == i: # 마지막인경우
            dp[i][j] = dp[i-1][j-1] + array[i][j]
        else: # 그외
            dp[i][j] = max(dp[i-1][j-1]+array[i][j], dp[i-1][j]+array[i][j])

print(max(dp[N-1]))