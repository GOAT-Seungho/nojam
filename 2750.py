# 2750 : 수 정렬하기

# code for submitting
N = int(input())
result = sorted([int(input()) for _ in range(N)])

for i in range(N):
    print(result[i])