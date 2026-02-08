import sys
input = sys.stdin.readline

answer1 = 0
answer2 = 0

level_grade = [60,100,140,200,250]
N = int(input())
level_list = [int(input()) for _ in range(N)]
level_list.sort(reverse=True)
cnt = min(42, len(level_list))

for i in range(cnt):
    answer1 += level_list[i]
    for j in level_grade:
        if level_list[i] >= j:
            answer2 += 1
        else:
            break

print(answer1, answer2)