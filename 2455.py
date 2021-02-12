# 2455 : 지능형 기차

# code for submitting
nums = 0
nums_record = []

for _ in range(4):
    O, I = map(int, input().split())
    nums -= O
    nums += I
    nums_record.append(nums)

print(max(nums_record))