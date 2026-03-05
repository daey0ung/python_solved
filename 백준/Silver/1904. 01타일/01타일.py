N = int(input())
array = [0]*1000001
array[1], array[2] = 1,2
for i in range(3,N+1):
    array[i] = (array[i-1]+array[i-2]) %15746
    
print(array[N])