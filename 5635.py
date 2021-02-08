# 5635 : 생일

# code for mitting
n = int(input())
students = []

for _ in range(n):
    name, day, month, year = map(str, input().split())
    if (int(month) < 10):
        month = '0' + month
    if (int(day) < 10):
        day = '0' + day
    students.append([name, int(year+month+day)])

    students = sorted(students, key = lambda x: x[1])

print(students[-1][0], students[0][0], sep="\n")


# another method
# import sys
# sys.stdin = open("input.txt", 'r')

# people = {}
# for _ in range(int(input())):
#     data = input.split()
#     people[data[0]] = [int(data[3]), int(data[2]), int(data[1])]
# s = sorted(people.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2]))
# print(s[0][0])
# print(s[-1][0])