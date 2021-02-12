# 2747 : 피보나치 수

# code for submitting
n = int(input())
a, b = 0, 1
for _ in range(n):
    a, b = b, a+b

print(a)