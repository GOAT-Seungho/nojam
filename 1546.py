# 1546 : 평균

# code for submitting
N = int(input())
scores = list(map(int, input().split()))
M = max(scores)

temp = list(map(lambda x: x / M * 100, scores))

print(sum(temp) / N)