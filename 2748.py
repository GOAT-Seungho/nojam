# 2748 : 피보나치 수 2

# code for submitting
def fibo(n):
    if n < 2:
        return n

    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    
    return b


n = int(input())
print(fibo(n))