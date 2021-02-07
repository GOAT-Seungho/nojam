# 10988 : 팰린드롬인지 확인하기

# 팰린드롬 : 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어


# code for submitting
word = str(input())
pelin = str()

for i in range(-1, -(len(word) + 1), -1):
    pelin += word[i]

if (word == pelin):
    print(1)
else:
    print(0)


# solution
# word = list(str(input()))

# if list(reversed(word)) == word:
#     print(1)
# else:
#     print(0)