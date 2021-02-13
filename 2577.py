# 2577 : 숫자의 개수

# code for submitting
A, B, C = int(input()), int(input()) ,int(input()) 

temp = list(str(A * B * C))

for i in range(10):
    print(temp.count(str(i)))