# 2576 : 홀수

# code for submitting
nums = list(filter(lambda x: x%2==1, [int(input()) for _ in range(7)]))

if not (nums):
    print(-1)
else:
    print(sum(nums), min(nums), sep="\n")