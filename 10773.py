# 10773 : 제로

# code for submitting
K = int(input())
nums = []

for _ in range(K):
    temp = int(input())
    if (temp == 0):
        nums.pop()
    else:
        nums.append(temp)

print(sum(nums))