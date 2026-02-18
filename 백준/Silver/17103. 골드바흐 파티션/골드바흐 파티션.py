M = 1000000

primes = [0, 0] + [1] * (M-1)
for i in range(2, int(M**0.5)+1):
    if primes[i]:
        for j in range(i*i, M+1,i):
            primes[j] = 0

T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    for p in range(2, N//2+1):
        if primes[p] and primes[N-p]:
            count += 1
    print(count)
