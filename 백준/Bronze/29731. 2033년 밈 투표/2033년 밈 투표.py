S = [
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop'
]

N = int(input())

for _ in range(N):
    A = input().strip()
    if A not in S:
        print('Yes')
        exit()

print('No')