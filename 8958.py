# 8958 : OX퀴즈

# code for submitting
N = int(input())

for _ in range(N):
    test = str(input())
    succession = 0
    score = 0

    for i in range(len(test)):
        if (test[i] == 'O'):
            succession += 1
            score += succession
        else:
            succession = 0

    print(score)