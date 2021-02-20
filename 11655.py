# 11655 : ROT13

# code for submitting
S = str(input())
rot13 = ''

for i in range(len(S)):
    # A - M, a - m
    if (65 <= ord(S[i]) <= 77 or 97 <= ord(S[i]) <= 109):
        rot13 += chr(ord(S[i]) + 13)
    
    # N - Z, n - z
    elif (78 <= ord(S[i]) <= 90 or 110 <= ord(S[i]) <= 122):
        rot13 += chr(ord(S[i]) - 13)

    # 공백, 숫자인 경우
    else:
        rot13 += S[i]

print(rot13)