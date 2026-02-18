def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    i = int(input())
    while True:
        if is_prime(i):
            print(i)
            break
        i += 1