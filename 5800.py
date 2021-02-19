# 5800 : 성적 통계

# code for submitting
K = int(input())

for i in range(K):
    temp = list(map(int, input().split()))
    N = temp[0]
    scores = sorted(temp[1:], reverse=True)

    biggest_gap = 0
    for j in range(N-1):
        if (scores[j] - scores[j+1] > biggest_gap):
            biggest_gap = scores[j] - scores[j+1]

    print("Class %d" % (i+1))
    print("Max %d, Min %d, Largest gap %d" % (max(scores), min(scores), biggest_gap))