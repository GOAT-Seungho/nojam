# 2446 : 별 찍기-9

# code for submitting
N = int(input())

for i in range(1, N):
    print(("*"*(2*(N-i)+1)).rjust(2*N-i))

for i in range(1, N+1):
    print(("*"*(2*i-1)).rjust(N+i-1))