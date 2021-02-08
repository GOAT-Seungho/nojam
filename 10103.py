# 10103 : 주사위 게임

# code for submitting
n = int(input())
c_score, s_score = 100, 100

for i in range(n):
    c, s = map(int, input().split())

    if (c > s):
        s_score -= c
    elif (s > c):
        c_score -= s

print(c_score, s_score, sep = '\n')