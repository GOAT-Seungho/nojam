# 1357 : 뒤집힌 덧셈

# code for submitting
def Rev(x):
    return int(str(x)[::-1])

X, Y = input().split()
print(Rev(Rev(X) + Rev(Y)))