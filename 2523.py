# 2523 : 별 찍기-13

# code for submitting
N = int(input())

for i in range(1, N):
    print("*" * i)

for i in range(1, N+1):
    print("*" * (N-i+1))