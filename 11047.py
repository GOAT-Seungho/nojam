# 11047 : 동전 0

# code for submitting
N, K = map(int, input().split())
A = sorted([int(input()) for _ in range(N)], reverse=True)

coin = 0

for i in range(N):
    if (K < A[i]):
        continue
    coin += K // A[i]
    K %= A[i]

print(coin)