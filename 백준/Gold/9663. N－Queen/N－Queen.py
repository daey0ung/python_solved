N = int(input())
board = [0] * N
count = 0

def is_safe(row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(row - i) == abs(col - board[i]):
            return False
    return True

def backtrack(row):
    global count
    if row == N:
        count += 1
        return
    
    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            backtrack(row + 1)

backtrack(0)
print(count)