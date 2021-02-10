# 2522 : 별 찍기-12

# code for submitting
N = int(input())

for i in range(1, N):
    print(("*" * i).rjust(N))

for i in range(1, N+1):
    print(("*" * (N-i+1)).rjust(N))