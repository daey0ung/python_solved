alphabet = [
    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z'
]

N = input().strip()
for s in N:
    print(alphabet[ord(s)-65-3], end='')