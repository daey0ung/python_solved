import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

arr_sort = sorted(set(arr))
dic = {arr_sort[i] : i for i in range(len(arr_sort))}

for i in arr:
    print(dic[i], end=' ')