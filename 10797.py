# 10797 : 10부제

# code for submitting
a = int(input()) % 10
print(len(list(filter(lambda x: x == a, map(int, input().split())))))
