N = int(input())
for _ in range(N):
    A = input()
    stack = []
    for a in A:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(a)
                break
    if len(stack)==0:
        print('YES')
    else:
        print('NO')