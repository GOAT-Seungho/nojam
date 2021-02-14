# 5054 : 주차의 신

# code for submitting
t = int(input())

for _ in range(t):
    n = int(input())
    stores = sorted(list(map(int, input().split())))
    diff = 0
    for i in range(1, n):
        diff += stores[i]-stores[i-1]
    
    print(diff * 2)