# 2581 : 소수

# code for submitting
M = int(input())
N = int(input())
res_list = []

for i in range(M, N+1):
    if i == 1:
        continue

    if i == 2:
        res_list.append(i)
        continue

    for j in range(2, i):
        if (i % j == 0):
            break
    
    if (j == i - 1):
        res_list.append(i)

if not (res_list):
    print(-1)
else:
    print(sum(res_list), min(res_list), sep="\n")