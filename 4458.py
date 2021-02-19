# 4458 : 첫 글자를 대문자로

# code for submitting
N = int(input())

for _ in range(N):
    s = str(input())
    print(s[0].upper() + s[1:])