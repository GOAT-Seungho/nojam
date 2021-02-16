# 2693 : N번째 큰 수

# code for submitting
T = int(input())
for _ in range(T):
    nums = sorted(list(map(int, input().split())))
    print(nums[-3])