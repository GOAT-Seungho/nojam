# 10987 : 모음의 개수

# code for submitting
word = str(input())
vowel = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in range(len(word)):
    if (word[i] in vowel):
        count += 1

print(count)