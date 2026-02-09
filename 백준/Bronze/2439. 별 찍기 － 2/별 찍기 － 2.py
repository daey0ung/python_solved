# 2439번
# 반복 횟수 N
N = int(input())

for i in range(N):
    # i+1만큼 별 출력하기
    s = '*'*(i+1)

    # 문자열의 왼쪽에 지정된 공백을 채워 전체 자릿수에 맞게 오른쪽 정렬
    print(s.rjust(N))