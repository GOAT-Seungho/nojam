# 10162 : 전자레인지

# code for submitting
A, B, C = 0, 0, 0

T = int(input())

while True:
    if (T >= 300):
        A += T // 300
        T %= 300
    elif (T >= 60):
        B += T // 60
        T %= 60
    else:
        C += T // 10
        T %= 10
        if (T != 0):
            print(-1)
            break
    
    if (T == 0):
        print(A, B, C)
        break


# solution
# T = int(input())

# if T % 10 != 0:
#     print(-1)
# else:
#     A = B = C = 0
#     A = T // 300
#     B = (T % 300) // 60
#     C = (T % 300) % 60 // 10
#     print(A, B, C)