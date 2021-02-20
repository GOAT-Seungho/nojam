# 1676 : 팩토리얼 0의 개수

# code for submitting
def factorial(x):
    if x <= 2:
        return x
    else:
        return x * factorial(x-1)

N = int(input())
N_fac = str(factorial(N))
count = 0

for i in range(-1, -(len(N_fac)), -1):
    if (N_fac[i] == '0'):
        count += 1
    else:
        break

print(count)