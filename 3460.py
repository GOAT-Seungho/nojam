# 3460 : 이진수

# code for submitting
T = int(input())

for _ in range(T):
    n = int(input())
    n_bin = format(n, 'b') # string
    n_bin_reverse = n_bin[::-1]

    for i in range(len(n_bin_reverse)):
        if (n_bin_reverse[i] == '1'):
            print(i, end=" ")