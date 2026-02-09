dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = input()
count = 0
for i in range(len(S)):
    for j in range(len(dial)):
        if S[i] in dial[j]:
            count += j + 2 + 1
print(count)