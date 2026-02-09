# 11021번
# 반복 횟수 T
T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a+b}')