S = input()

d = {}
for i in range(ord('a'), ord('z')+1):
    d[i] = -1

for i in range(len(S)):
    if S[i] not in S[:i]:
        d[ord(S[i])] = i

print(*d.values())