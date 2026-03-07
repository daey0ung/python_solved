S = input()
N = int(input())
count = 0
for _ in range(N):
    if input() == S:
        count += 1

print(count)