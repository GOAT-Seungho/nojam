# 3040 : 백설 공주와 일곱 난쟁이

# code for submitting
nums = [int(input()) for _ in range(9)]
breaker = False

for i in range(9):
    for j in range(i+1, 9):
        if (nums[i] + nums[j] == sum(nums) - 100):
            breaker = True
            break
    if breaker:
        break

for k in range(9):
    if (nums[k] == nums[i] or nums[k] == nums[j]):
        continue
    print(nums[k])