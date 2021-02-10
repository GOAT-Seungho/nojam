# 10833 : 사과

# code for submitting
N = int(input())
remain = 0

for _ in range(N):
    students, apples = map(int, input().split())
    remain += apples % students

print(remain)