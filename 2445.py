# 2445 : 별 찍기-8

# code for submitting
N = int(input())

for i in range(1, N):
    print('*' * i + ' ' * (2*N-2*i) + '*' * i)

print('*' * 2*N)

for i in range(N-1, 0, -1):
    print('*' * i + ' ' * (2*N-2*i) + '*' * i)