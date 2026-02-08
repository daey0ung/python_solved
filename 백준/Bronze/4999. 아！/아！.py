import sys
input = sys.stdin.readline
N = input().strip()
M = input().strip()
if N.count('a') >= M.count('a'):
    print('go')
else:
    print('no')