max_val = -1
max_r, max_c = 0, 0

for r in range(9):
    row = list(map(int, input().split()))
    for c in range(9):
        if row[c] > max_val:
            max_val = row[c]
            max_r, max_c = r, c

print(max_val)
print(max_r + 1, max_c + 1)
