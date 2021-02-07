# 5086 : 배수와 약수

# code for submitting
while True:
    A, B = map(int, input().split())

    if (A == 0 and B == 0):
        break

    # 1. 첫 번째 숫자가 두 번째 숫자의 약수 -> factor
    if (B % A == 0):
        print('factor')
    
    # 2. 첫 번째 숫자가 두 번째 숫자의 배수 -> multiple
    elif (A % B == 0):
        print('multiple')
    
    # 3. 둘 다 아닌 경우 -> neither
    else:
        print('neither')