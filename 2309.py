# 2309 : 일곱 난쟁이

# code for submitting
height = sorted([int(input()) for _ in range(9)])

sum = sum(height)

breaker = False
a = b = int()

for i in range(9):
    for j in range(i+1, 9):
        if (height[i] + height[j] == sum - 100):
            a, b = height[i], height[j]
            breaker=True
            break
    if breaker == True:
        break

height.remove(a)
height.remove(b)

for i in range(len(height)):
    print(height[i])