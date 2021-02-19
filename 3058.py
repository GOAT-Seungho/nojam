# 3058 : 짝수를 찾아라

# code for submitting
T = int(input())

for _ in range(T):
    nums = list(map(int, input().split()))
    nums = list(filter(lambda x: x%2 == 0, nums))

    print(sum(nums), min(nums))