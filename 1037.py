# 1037 : 약수

# code for submitting
i = int(input())
nums = sorted(list(map(int, input().split())))

if (i == 1):
    print(nums[0] ** 2)
else:
    print(nums[0] * nums[-1])


# solution

# i = int(input())
# nums = list(map(int, input().split()))

# print(max(nums) * min(nums))