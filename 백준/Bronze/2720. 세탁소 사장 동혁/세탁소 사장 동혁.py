import sys
input = sys.stdin.readline

change_list = [25, 10, 5, 1]

T = int(input())

for _ in range(T):
    N = int(input())

    for i in change_list:
        print(N // i, end=' ')
        N = N % i

    print()