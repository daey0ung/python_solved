L = int(input())
A = list(input())
MOD = 1234567891
answer=0
for idx, i  in enumerate(A):
    answer += (ord(i)-96) * (31**idx)
    answer %= MOD
print(answer)