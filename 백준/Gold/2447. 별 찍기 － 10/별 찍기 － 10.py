def star(n):
    if n == 1:
        return ['*']
    
    arr = star(n//3)
    result = []

    for i in arr:
        result.append(i*3)
    for i in arr:
        result.append(i + ' '*(n//3) + i)
    for i in arr:
        result.append(i*3)
    return result

N = int(input())
print('\n'.join(star(N)))