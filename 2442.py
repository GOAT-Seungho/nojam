# 2442 : 별 찍기-5

# code for submitting
N = int(input())

for i in range(1, N+1):
    print(("*"*(2*i-1)).rjust(N+i-1))



# 출력 형태가 잘못된 code
# for i in range(1, N+1):
#     print(("*" *(2*i-1)).center(2*N-1))