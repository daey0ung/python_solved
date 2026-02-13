N = input()

S = ''

for i in range(1,100001):
    S += str(i)

print(S.index(N)+1)