stack, answer = [], []
cnt = 1
check = True

N = int(input())
for i in range(N):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        answer.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        check = False
        break

if check:
    print('\n'.join(answer))
else:
    print('NO')
