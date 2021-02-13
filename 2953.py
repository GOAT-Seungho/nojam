# 2953 : 나는 요리사다

# code for submitting
scores = [sum(list(map(int, input().split()))) for _ in range(5)]
print(scores.index(max(scores))+1, max(scores))