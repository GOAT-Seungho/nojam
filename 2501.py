# 2501 : 약수 구하기

# code for submitting
N, K = map(int, input().split())
res_list = []

for i in range(1, N+1):
    if not (N % i):
        res_list.append(i)

if (len(res_list) < K):
    print(0)
else:
    print(res_list[K-1])