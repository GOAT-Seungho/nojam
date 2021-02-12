# 2506 : 점수계산

# code for submitting
N = int(input())
answer = list(map(int, input().split()))

succession = score = 0

for i in range(len(answer)):
    if answer[i]:
        succession += 1
        score += succession
    else:
        succession = 0

print(score)