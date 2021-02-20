# 5218 : 알파벳 거리

# code for submitting
alphabet = dict(
    A = 1, B = 2, C = 3, D = 4, E = 5, F = 6, 
    G = 7, H = 8, I = 9, J = 10, K = 11, L = 12, 
    M = 13, N = 14, O = 15, P = 16, Q = 17, R = 18, 
    S = 19, T = 20, U = 21, V = 22, W = 23, X = 24, 
    Y = 25, Z = 26
)

def distance(x, y):
    if (alphabet[y] >= alphabet[x]):
        return alphabet[y] - alphabet[x]
    else:
        return alphabet[y] + 26 - alphabet[x]


T = int(input())

for j in range(T):
    X, Y = map(str, input().split())
    
    print("Distances: ", end="")

    for i in range(len(X)):
        print(distance(X[i], Y[i]), end=" ")
    if (j != T - 1):
        print()