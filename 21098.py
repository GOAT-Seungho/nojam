# 21098 : 첼시를 도와줘!

# code for submitting
n = int(input())

for _ in range(n):
    p = int(input())
    most_expensive = {}

    for _ in range(p):
        C, player = map(str, input().split())
        most_expensive[int(C)] = player

    print(most_expensive[max(most_expensive.keys())])
