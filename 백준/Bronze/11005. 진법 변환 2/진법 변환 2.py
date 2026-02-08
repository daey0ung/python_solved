num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int,input().split())
answer = ''
if N==0:
    print(0)
else:
    while N != 0:
        a = N % B
        N = N //B
        answer = num_list[a] + answer
    print(answer)