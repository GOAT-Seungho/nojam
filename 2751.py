# 2751 : 수 정렬하기 2

# code for submitting
import sys

N = int(input())

nums = sorted([int(sys.stdin.readline()) for _ in range(N)])

for i in range(N):
    print(nums[i])