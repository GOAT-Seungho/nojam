# 2441 : 별 찍기-4

# code for submitting
N = int(input())

for i in range(N):
    print(('*' * (N-i)).rjust(N))



# solution
# a=int(input())
# for i in range(1,a+1):
#     print(" "*(i-1) + "*"*(a-i+1))