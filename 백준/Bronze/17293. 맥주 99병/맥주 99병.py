N = int(input())
for i in range(N):
    if N-i == 1:
        print(f'{N-i} bottle of beer on the wall, {N-i} bottle of beer.')
        print('Take one down and pass it around, no more bottles of beer on the wall.')
    elif N-i == 2:
        print(f'{N-i} bottles of beer on the wall, {N-i} bottles of beer.')
        print(f'Take one down and pass it around, {N-i-1} bottle of beer on the wall.')
    else:
        print(f'{N-i} bottles of beer on the wall, {N-i} bottles of beer.')
        print(f'Take one down and pass it around, {N-i-1} bottles of beer on the wall.')

    print()

print('No more bottles of beer on the wall, no more bottles of beer.')
if N == 1:
    print(f'Go to the store and buy some more, {N} bottle of beer on the wall.')
else:
    print(f'Go to the store and buy some more, {N} bottles of beer on the wall.')