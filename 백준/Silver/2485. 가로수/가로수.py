def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

N = int(input())
points = [int(input()) for _ in range(N)]

intervals = []
for i in range(1,N):
    intervals.append(points[i]-points[i-1])

g = intervals[0]
for i in range(1, len(intervals)):
    g = gcd(g, intervals[i])

total = points[-1] - points[0]
answer = (total // g) + 1 - N

print(answer)