import sys
input = sys.stdin.readline

try:
    while True:
        x = 0
        answer = ''
        s, t = input().split()
        for i in t:
            if len(answer) < len(s) and i == s[x]:
                answer += i
                x += 1

        if answer == s:
            print('Yes')
        else:
            print('No')
except:
    exit()