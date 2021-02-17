# 10809 : 알파벳 찾기

# code for submitting
S = str(input())
alphabet = dict(
    a = -1, b = -1, c = -1, d = -1, e = -1, f = -1, 
    g = -1, h = -1, i = -1, j = -1, k = -1, l = -1, 
    m = -1, n = -1, o = -1, p = -1, q = -1, r = -1, 
    s = -1, t = -1, u = -1, v = -1, w = -1, x = -1, 
    y = -1, z = -1
)

for i in range(len(S)):
    if (alphabet[S[i]] == -1):
        alphabet[S[i]] = i

for i in range(26):
    print(list(alphabet.values())[i], end=" ")

# solution
# word = input()
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위

# for x in alphabet :
#     print(word.find(chr(x))) 