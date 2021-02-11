# 2921 : 도미노

# code for submitting
N = int(input())
sum = 0

for i in range(N+1):
    for j in range(i, N+1):
        sum += i + j

print(sum)

# another solution
# N = int(input())
# print(((N) * (N+1) * (N+2)) // 2)