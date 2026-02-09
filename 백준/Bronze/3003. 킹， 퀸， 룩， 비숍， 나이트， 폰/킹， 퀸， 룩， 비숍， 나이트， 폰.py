chess_list = [1,1,2,2,2,8]
input_list = list(map(int,input().split()))
for i in range(len(input_list)):
    print(chess_list[i]-input_list[i], end=' ')