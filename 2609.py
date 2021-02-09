# 2609 : 최대공약수와 최소공배수

# code for submitting
def lcm(a,b):
    d = gcd(a, b)
    return d * (a // d) * (b // d)

def gcd(a, b):
    return gcd(b%a, a) if b % a else a

A, B = map(int, input().split())
print(gcd(A, B), lcm(A, B), sep="\n")

# solution 1
# a, b = map(int, input().split())
# 
# def gcd(x,y):
#     mod = x % y
#     while mod >0:
#         x = y
#         y = mod
#         mod = x % y
#     return y    
#     
# def lcm(x, y):
#     return x * y // gcd(x,y)
# 
# print(gcd(a, b))
# print(lcm(a, b))

# solution 2
# while b != 0: 
#     a = a % b 
#     a, b = b, a 
# gcd 
# print(a) 
# lcm 
# print(A*B//a)
