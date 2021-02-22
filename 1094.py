# 1094 : 막대기

# code for submitting
X = int(input())

sticks = [64]

if (X < 64):
    while True:
        a = b = sticks.pop() // 2
        sticks.append(a)

        if not (sum(sticks) >= X):
            sticks.append(b)

        if (sum(sticks) == X):
            break
    
    print(len(sticks))
    
else:
    print(1)