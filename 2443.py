# 2443 : 별 찍기-6

# code for submitting
N = int(input())

for i in range(1, N+1):
    print(("*"*(2*(N-i)+1)).rjust(2*N-i))