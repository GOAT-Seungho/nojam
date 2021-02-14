# 2822 : 점수 계산

# code for submitting
scores = [[int(input()), i] for i in range(1, 9)]
scores_top_5 = sorted(scores, key=lambda x : x[0], reverse=True)[:5]
scores_sorted = sorted(scores_top_5, key=lambda x: x[1])

print(sum(list(map(lambda x: x[0], scores_top_5))))
for i in range(5):
    print(scores_sorted[i][1], end=" ")
