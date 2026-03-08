T= int(input())
for _ in range(T):
    N = int(input())
    answer = 0
    while N != 1:
        if N%2:
            N = N//2 + 1
            answer +=1
        else:
            N = N//2
    print(answer)