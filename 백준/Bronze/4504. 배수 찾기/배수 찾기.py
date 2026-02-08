import sys
input = sys.stdin.readline

N = int(input())

while True:
    M = int(input())
    if M == 0:
        break
    
    if M%N == 0:
        print(f'{M} is a multiple of {N}.')
    else:
        print(f'{M} is NOT a multiple of {N}.')