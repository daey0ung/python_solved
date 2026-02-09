N = int(input())
for i in range(N):
    s = input()
    cnt = 0
    point = 0
    for j in s:
        if j == 'O':
            cnt+=1
            point += int(cnt)
        else:
            cnt = 0
    print(point)