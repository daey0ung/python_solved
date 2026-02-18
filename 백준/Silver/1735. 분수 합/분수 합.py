def gcd(a,b):
    while b:
        a, b = b, a% b
    return a

A, B = map(int, input().split())
C, D = map(int, input().split())

# 분자
num = A*D+C*B

# 분모
den = B*D

g = gcd(den,num)
print(num//g,den//g)