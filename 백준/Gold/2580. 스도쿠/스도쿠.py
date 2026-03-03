import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)] 
blank_coord = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def check(y, x, check_num):
    # 행, 열에 같은 값이 있는지 확인
    for i in range(9):
        if sudoku[y][i] == check_num or sudoku[i][x] == check_num:
            return False
    
    # 3x3에 같은 값이 있는지 확인
    for i in range(3):
        for j in range(3):
            if sudoku[y//3*3+i][x//3*3+j] == check_num:
                return False
    
    return True

def solve(n):
    if n == len(blank_coord):
        for row in sudoku:
            print(*row)
        exit() # 해를 찾을 경우 종료
    
    for check_num in range(1, 10):
        y, x = blank_coord[n]
        if check(y, x, check_num):
            sudoku[y][x] = check_num
            solve(n+1)
            sudoku[y][x] = 0

solve(0)