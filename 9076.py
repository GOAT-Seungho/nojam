# 9076 : 점수 집계

# code for submitting
T = int(input())

for _ in range(T):
    scores = sorted(list(map(int, input().split())))
    scores = scores[1:-1]
    if (max(scores) - min(scores) >= 4):
        print("KIN")
    else:
        print(sum(scores))
