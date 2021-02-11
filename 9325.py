# 9325 : 얼마?

# code for submitting
T = int(input())

for _ in range(T):
    s = int(input())
    sum = s

    n = int(input())

    for _ in range(n):
        q, p = map(int, input().split())
        sum += q*p
    
    print(sum)
