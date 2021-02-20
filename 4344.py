# 4344 : 평균은 넘겠지

# code for submitting
C = int(input())

for _ in range(C):
    temp = list(map(int, input().split()))
    N = temp[0]
    scores = temp[1:]

    avg = sum(scores) / N

    high = list(filter(lambda x: x > avg, scores))

    print("%.3f" % ((len(high) / N) * 100) + "%")