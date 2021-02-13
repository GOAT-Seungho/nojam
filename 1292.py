# 1292 : 쉽게 푸는 문제

# code for submitting
nums = []
for i in range(1, 46):
    for _ in range(i):
        nums.append(i)

A, B = map(int, input().split())
print(sum(nums[A-1:B]))

# for i in range(1, 46):
#     number_list += [i] * i