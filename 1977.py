# 1977 : 완전제곱수

M, N = int(input()), int(input())
perfect = []
for i in range(1, 101):
    if (M <= i ** 2 <= N):
        perfect.append(i**2)

if (len(perfect) == 0):
    print(-1)
else:
    print(sum(perfect), min(perfect), sep="\n")