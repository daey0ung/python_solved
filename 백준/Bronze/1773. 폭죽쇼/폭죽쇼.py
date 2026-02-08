T, C = map(int, input().split())
time = [0] * (C+1)

for _ in range(T):
    n = int(input())
    if n == 1:
        print(C)
        exit()
    time[n::n] = [1]*(C//n)

print(sum(time))