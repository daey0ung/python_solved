while True:
    A = input()
    if A == '.':
        break

    stack=[]

    for a in A:
        if a=='(' or a=='[':
            stack.append(a)
        elif a==')':
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(a)
                break
        elif a==']':
            if len(stack)!=0 and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(a)
                break

    if len(stack)==0:
        print('yes')
    else:
        print('no')