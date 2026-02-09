l = list(range(1, 31))
try:
    while True:
        a = int(input())
        l.remove(a)
except:
    print(*l)   