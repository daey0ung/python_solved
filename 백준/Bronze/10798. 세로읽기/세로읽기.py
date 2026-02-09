a = []
for _ in range(5):
    a.append(list(input()))

for col in range(15):
    for row in range(5):
        if col < len(a[row]):
            print(a[row][col], end='')