import sys
input = sys.stdin.readline

while True:
    N = input().strip()
    if N == '0':
        break

    answer = 0
    factorial = 1
    for i in range(1, len(N)+1):
        factorial *= i
        answer += int(N[-i]) * factorial

    print(answer)