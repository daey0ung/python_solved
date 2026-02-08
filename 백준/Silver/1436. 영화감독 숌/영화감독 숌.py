# 1436번
N = int(input())
cnt = 0
answer = 666

while True:
    str_answer = str(answer)
    if "666" in str_answer:
        cnt += 1
    if N == cnt:
        break
    answer += 1

print(answer)