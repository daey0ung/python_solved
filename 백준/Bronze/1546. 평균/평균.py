a = int(input())
l = list(map(int, input().split()))
b = max(l)
for i in range(a):
    l[i] = l[i]/b*100
print(sum(l)/len(l))