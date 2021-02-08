# 10214 : Baseball

# code for submitting
T = int(input())

for _ in range(T):

    yonsei_score = korea_score = 0

    for i in range(9):
        yonsei, korea = map(int, input().split())
        yonsei_score += yonsei
        korea_score += korea

    if (yonsei_score > korea_score):
        print("Yonsei")
    elif (yonsei_score < korea_score):
        print("Korea")
    else:
        print("Draw")