asc = [1,2,3,4,5,6,7,8]
a = list(map(int, input().split()))
if a == asc:
    print('ascending')
elif a == asc[::-1]:
    print('descending')
else:
    print('mixed')