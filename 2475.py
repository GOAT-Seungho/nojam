# 2475 : 검증수

# code for submitting
nums = list(map(int, input().split()))
nums_square = list(map(lambda x: x**2, nums))
res = sum(nums_square) % 10

print(res)