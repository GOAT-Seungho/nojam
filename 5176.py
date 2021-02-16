# 5176 : 대회 자리

# code for submitting
K = int(input())

for _ in range(K):
    P, M = map(int, input().split())
    wanted = len(set([int(input()) for _ in range(P)]))
    print(P - wanted)
