import sys
input = sys.stdin.readline

x = 0
y = 0

for _ in range(3):
    a, b = map(int, input().split())
    x = x ^ a
    y = y ^ b

print(x, y)