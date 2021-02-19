# 5576 : 콘테스트

# code for submitting
W = sorted([int(input()) for _ in range(10)])
K = sorted([int(input()) for _ in range(10)])

W_score = W[-1] + W[-2] + W[-3]
K_score = K[-1] + K[-2] + K[-3]

print(W_score, K_score)