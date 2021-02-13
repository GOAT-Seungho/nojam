# 2460 : 지능형 기차 2

# code for submitting
nums = 0
nums_record = []

for _ in range(10):
    O, I = map(int, input().split())
    nums -= O
    nums += I
    nums_record.append(nums)

print(max(nums_record))