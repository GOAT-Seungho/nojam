# 2711 : 오타맨 고창영

# code for submitting
T = int(input())

for _ in range(T):
    index, words = input().split()
    index = int(index)
    result = words[:index-1] + words[index:]
    print(result)