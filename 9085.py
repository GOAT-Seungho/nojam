# 9085 : 더하기

# code for submitting
T = int(input())

for _ in range(T):
    N = int(input())

    print(sum(list(map(int, input().split()))))
