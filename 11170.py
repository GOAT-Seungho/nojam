# 11170 : 0의 개수

# code for submitting
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    count = 0
    
    for i in range(N, M+1):
        if '0' in str(i):
            count += str(i).count('0')
    
    print(count)
