N = int(input())
A = set(input().strip() for _ in range(N))
sorted_A = sorted(A, key=lambda x: (len(x), x))
print(*sorted_A, sep='\n')