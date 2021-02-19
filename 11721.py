# 11721 : 열 개씩 끊어 출력하기

# code for submitting
word = str(input())

for i in range(0, len(word), 10):
    if (i + 10 > len(word)):
        print(word[i:])
    else:
        print(word[i:i+10])