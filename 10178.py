# 10178 : 할로윈의 사탕

# code for submitting
T = int(input())

for _ in range(T):
    c, v = map(int, input().split())
    you, dad = divmod(c, v)
    print("You get %d piece(s) and your dad gets %d piece(s)." % (you, dad))