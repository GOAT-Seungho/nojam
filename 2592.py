# 2592 : 대표값

# code for submitting
nums = [int(input()) for _ in range(10)]
counts = [0 for _ in range(10)]
temp = dict()

for i in range(10):
    if (nums[i] in temp.keys()):
        temp[nums[i]] += 1
    else:
        temp[nums[i]] = 1

mode = [k for k, v in temp.items() if v == max(temp.values())]

print(int(sum(nums) / 10))
print(mode[0])

# solution
# numbers = [int(input()) for i in range(10)]
# print(sum(numbers)//10)
# print(max(numbers, key = numbers.count))