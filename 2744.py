# 2744 : 대소문자 바꾸기

# code for submitting
word = list(str(input()))

for i in range(len(word)):
    if (word[i].isupper()):
        word[i] = word[i].lower()
    else:
        word[i] = word[i].upper()

print(''.join(word))