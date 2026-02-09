n = int(input())
output=n
for i in range(n):
    a = input()
    for j in range(len(a)-1):
        if a[j] == a[j+1]:
            continue
        else:
            if a[j] in a[j+1:]:
                output -= 1
                break
print(output)