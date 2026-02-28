arr = [int(input()) for _ in range(5)]

if arr[0] < 0:
    print(abs(arr[0])*arr[2] + arr[3] + arr[1]*arr[4])
else:
    print((arr[1]-arr[0])*arr[4])