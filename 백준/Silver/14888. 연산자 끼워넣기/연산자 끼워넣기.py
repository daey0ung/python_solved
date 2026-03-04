import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split())) 
add, sub, mul, div = map(int, input().split())
max_result = -int(1e9)
min_result = int(1e9)

def dfs(total, n, add, sub, mul, div):
    global max_result, min_result
    if n == N:
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return
    
    if add:
        dfs(total+num_list[n], n+1, add-1, sub, mul, div)
    if sub:
        dfs(total-num_list[n], n+1, add, sub-1, mul, div)
    if mul:
        dfs(total*num_list[n], n+1, add, sub, mul-1, div)
    if div:
        dfs(int(total/num_list[n]), n+1, add, sub, mul, div-1)

dfs(num_list[0], 1, add,sub,mul,div)
print(max_result)
print(min_result)