# 10995 : 별 찍기-20

# code for submitting
N = int(input())

for i in range(1, N+1):
    if (i % 2 == 1):
        for j in range(1, 2*N):
            if (j % 2 == 1):
                print("*", end="")
            else:
                print(" ", end="")

    else:
        for j in range(1, 2*N+1):
            if (j % 2 == 1):
                print(" ", end="")
            else:
                print("*", end="")

    print()