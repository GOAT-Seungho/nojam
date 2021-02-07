# 9506 : 약수들의 합

# code for submitting
def p(n_list, n):
    print(n, '= ', end='')
    for i in range(len(n_list)):
        print(n_list[i], end='')
        if (i+1 != len(n_list)):
            print(' + ', end='')
        else:
            print()

while True:
    n = int(input())
    n_ali = []

    if (n == -1):
        break

    for i in range(1, n):
        if (n % i == 0):
            n_ali.append(i)
    
    if (sum(n_ali) == n):
        p(n_ali, n)
    else:
        print(n, "is NOT perfect.")


# solution 1
'''
100,000 이하의 완전수는 4개 밖에 존재하지 않는다. ㅋㅋㅋ
'''
# perfect_num = {6 : "6 = 1 + 2 + 3",
#                28 : "28 = 1 + 2 + 4 + 7 + 14",
#                496: "496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248",
#                8128 : "8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064"}

# num = int(input())
# while num != -1:
#     if num in perfect_num:
#         print(perfect_num[num])
#     else:
#         print("%s is NOT perfect." % (num))
#     num = int(input())


# solution 2
'''
print 문을 눈여겨 볼만 함.
'''

# import sys

# myList = []
# checkList = []
# col = []
# while True:
#     a = int(sys.stdin.readline())
#     if a == -1:
#         break
#     myList.append(a)

# for item in myList:
#     col = []
#     for i in range(1,(item)):
#         if (item % i) == 0:
#             col.append(i)
#     if sum(col) == item:
#         print(str(item)+ ' = ' + ' + '.join(map(str,col)))
#     else:
#         print(str(item) + ' is NOT perfect.')