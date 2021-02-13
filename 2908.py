# 2908 : 상수

# code for submitting
A, B = map(list, input().split())
a = b = ''

for i in range(3):
    a += A.pop()
    b += B.pop()

a, b = int(a), int(b)

print(max(a, b))

# solution
# a, b = input().split()

# a = int(a[::-1])
# b = int(b[::-1])

# if (a > b) :
#     print(a)
# else:
#     print(b)