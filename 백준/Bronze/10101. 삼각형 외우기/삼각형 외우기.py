import sys
input = sys.stdin.readline

degree = [int(input()) for _ in range(3)]

sum_d = sum(degree)
set_d = set(degree)

if sum_d != 180:
    print('Error')
elif len(set_d) == 1:
    print('Equilateral')
elif len(set_d) == 2:
    print('Isosceles')
else:
    print('Scalene')