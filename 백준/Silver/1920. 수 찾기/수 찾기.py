import sys
input = sys.stdin.readline

N = int(input())
N_list = set(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

cnt_list = []

for i in M_list:
    if i in N_list:
        cnt_list.append(1)
    else:
        cnt_list.append(0)

for i in cnt_list:
    print(i)