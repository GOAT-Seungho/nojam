# 9295 : 주사위

# code for submitting
T = int(input())

for i in range(T):
    print("Case %d: %d" % (i+1, sum(map(int, input().split()))))
