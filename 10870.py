# 10870 : 피보나치 수 5

# code for submitting
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input())

print(fibo(n))