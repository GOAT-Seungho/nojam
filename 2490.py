# 2490 : 윷놀이

# code for submitting
# 배 : 0, 등 : 1

for i in range(3):
    res = sum(list(map(int, input().split())))
    if (res == 0):
        print("D")
    elif (res == 1):
        print("C")
    elif (res == 2):
        print("B")
    elif (res == 3):
        print("A")
    else:
        print("E")